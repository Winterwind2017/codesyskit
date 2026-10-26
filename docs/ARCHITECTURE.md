# Architecture and the dependency order that actually works

## 1. What CODESYS gives us

| fact | measurement |
| --- | --- |
| `CODESYS.exe` is a **managed** .NET 4.8 launcher | REA: `managed=true`, 30 types / 276 methods, 0.5 MB |
| the engine is a plugin, not a COM server | `RegAsm /regfile`: 3 coclasses, none of them the engine |
| scripting is IronPython **2.7.12** | `ScriptLib\4.1.0.0` (515 stdlib modules) + `ScriptEngine.plugin 4.2.0.0` |
| the API is fully documented offline | `ScriptLib\Stubs\scriptengine\*.pyi`: 50 modules, 262 classes, 1395 `def` lines (636 plain methods + 733 property accessors) — full catalog in `docs/API-SURFACE.md` |
| the engine can run headless | `--profile="…" --noUI --runscript=…` |
| 1562 device descriptions ship with the install | `device_repository.get_all_devices()` |
| 870 IDE commands exist | `len(system.commands)` |

## 2. Why the service lives inside the CODESYS process

`ScriptEngine3.dll` references **25 assemblies** — 24 of them CODESYS` own
(`Engine`, `Objects`, `Online`, `DeviceObject`, `TextDocument`, `MessageService`, `ProjectArchive`,
`TaskConfig`, `UserManagement`, …). An in-process COM activation would have to load all of that
into the *client* process and would still not see the project the IDE has open. Hosting the engine
in a real headless IDE and talking to it over loopback gives:

* the live session (open project, unsaved edits, compile cache);
* zero client-side dependencies (standard library socket + json);
* no bitness problem (`ScriptEngine3.dll` is x86; the client may be 64-bit);
* no registry footprint.

## 3. The dependency order (each link measured)

```
1. CODESYS.exe --profile="<name>" --noUI --runscript=<generated server.py>
      ↑ the profile name must keep its literal quotes, see §4.1
2. scriptengine imports; system/projects/device_repository become live objects
3. device_repository.get_all_devices()        (1562 items; the collection is not subscriptable)
4. projects.create(path)                      → empty project
5. project.add("PLC", device.device_id)       → device + application appear
      ↑ two arguments, and device_id is a DeviceId object, not a name
6. project.active_application                 (fails with "需要一个非空的 Guid" before step 5)
7. application.create_program(name, language=ImplementationLanguages.st)
      ↑ without the ST guid you get the default language and your text is not what compiles
8. project.save() / projects.open(path)       (read-back judge)
9. application.create_task_configuration() → create_task(name) → task.pous.add(pou)
      ↑ WITHOUT THIS STEP build() COMPILES NOTHING AND REPORTS 0 ERRORS
10. application.build()                       → diagnostics on stderr, not in message storage
11. Service.compile() slices engine.stderr.log and parses C189/C9/C190 + the 编译完成 summary
```

Steps 5, 7, 9 and 10 are the ones that silently "succeed" when done in the wrong order or with the
wrong argument shape. Every one of them is covered by a unit or live test.

## 4. Engine constraints that shaped the code

### 4.1 The profile must keep its quotes

```
CODESYS.exe --profile=CODESYS V3.5 SP22 Patch 2 --noUI …   → exit 1
    启动参数 --noUI 模式, 请使用 --profile="profile name" 指定配置文件.

CODESYS.exe --profile="CODESYS V3.5 SP22 Patch 2" --noUI … → works
```

`subprocess.Popen(list)` re-quotes/escapes the argument, so the engine never sees the quotes.
`service.build_command_line()` therefore returns a **single command-line string**.

### 4.2 `print()` pollutes the IDE message list

In `--noUI` mode `print` is routed into `system.get_messages()`, so the server never prints: it
writes `service.log` and JSON replies.

### 4.3 The script must exit itself

Nothing closes the process for you; the generated script ends with `SYSTEM.exit(0)`.

### 4.4 IronPython 2.7 quirks

* `Socket.Accept()` returns a **single** `Socket`, not a `(socket, endpoint)` tuple;
* byte buffers are `Array.CreateInstance(Byte, n)` and are filled one char at a time;
* no `os.makedirs(exist_ok=…)`, no f-strings, no `bytes` literal semantics;
* file writes need `codecs.open(path, "w", "utf-8")` or Chinese text raises `UnicodeEncodeError`.

### 4.5 One request per connection

The accept loop is single threaded: a keep-alive connection would block every other client until
it closed (measured: 10 s timeout for the second client). The server reads one line, answers,
closes; the client opens a fresh connection per call (≈1 ms on loopback).

### 4.6 `ScriptTextDocument.text` is read-only

Writes go through `replace(offset, length, text)` (or `remove(offset, length)` + `append(text)`;
`remove` takes **(offset, length)** — reversed arguments silently turn the document into old+new).

## 4b. Findings from the extended surface sweep

* **`system.commands` is the general escape hatch**: 870 commands, each with `name`, `guid`,
  `description`, `tokens` and `execute()`. `execute` is judged the same way as `build` — from the
  engine's stderr window — so `service.run_command(client, "重新编译")` returns
  `{ok, errors, warnings, messages}`.
* **Libraries are scriptable**: `libman.get_libraries()` lists the referenced ones and
  `add_library("Standard")` really appends to that list (verified twice); the global
  `librarymanager.get_all_libraries()` reports **537** available libraries.
* **Exchange works, with one shape constraint**: `export_xml([application])` writes 1 KB of
  PLCopenXML, `export_xml([device])` 2 KB, `export_native` 23 KB, `save_archive` 5.4 MB; the
  project root itself raises a cast error, so the default target is the active application.
  `import_xml` succeeds into an **empty** project (children 2 → 3) and fails with
  `未找到可导入的对象` when the target already has the same object.
* **`export_doc` is a silent no-op in `--noUI`** (returns normally, writes nothing) — the command
  reports `E_UNAVAILABLE` instead of pretending.
* **No `create_symbol_configuration`** on application or device in this version
  (`AttributeError`), so symbol-config creation is out of scope here.
* **Two transport bugs found by the sweep** and fixed: replies were written as raw char codes
  (`Cannot convert int(36333) to Byte` for any Chinese reply) and `Socket.Send` was assumed to send
  everything. Replies are now UTF-8 encoded and sent in a loop; requests are decoded as UTF-8.
* **Path building must avoid identity comparisons**: the engine hands out fresh wrapper objects, so
  `/A/B/C` paths are built from names until the unnamed project root; mutating commands refuse a
  path that resolves to the root.

## 5. Process model

```
codesyskit (CLI / library)
  └── Service                        owns the child process, state dir, engine.stderr.log
        └── CODESYS.exe  (headless)  runs server.py (generated, token baked in)
              ├── service.json       port, token, pid, banner  (read by clients)
              ├── service.log        server-side trace
              └── engine.stderr.log  compiler diagnostics       (parsed by Service.compile)
```

`start` waits for `service.json` **and** a successful `ping`, so a returned state means the service
is usable, not merely launched. `stop` sends `quit`, waits, then `taskkill` if needed.
