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

## 4c. Online: the chain that finally worked

```
gateway services?          blocked: `sc start` -> Access is denied (DACL gives IU no start right)
plain-process launch?      GatewayService.exe / CODESYSControlService.exe exit at once (need SCM)
add_new_gateway(...)       works: 3 drivers (SharedMemory / TCP-IP / Automation Server), config_params readable
set_gateway_and_address()  works: an IP string is normalised to 0127.0000.0000.0001; "localhost" is rejected
login with TCP gateway     fails: 网络错误:没有到达主机的路由 (nothing listens on 1217)
device.set_simulation_mode(True)  <- THE ANSWER: gateway auto-assigned, address 0000, login succeeds
```

Measured on the working path: `application_state` goes `none → run`, the cyclic task increments a
counter (8 → 68 in 1.2 s), a write of 1000 reads back 1007, five monitored samples step by 20,
`stop`/`start` toggle the state, `create_boot_application()` returns normally.

Two traps found on the way:

* **re-login is a download**: creating a fresh `OnlineApplication` and logging in for every read
  restarts the program and resets values to 0 (first attempts read `0, 0`). One `OnlineApplication`
  is cached per project (`ONLINE`) and reused while `is_logged_in`.
* **`set_prepared_value` wants a string** (`42` raises `TypeError: expected str, got int`), so
  `online.write` stringifies the value before preparing it.

## 4d. What the second sweep found (offline, no PLC)

* **The IDE command list is a map of the product**: 832 unique commands in 90 families
  (`recon/commands.json`, `docs/COMMANDS.md`). Families with real weight: `network` 78,
  `visual` 68, `online` 54, `cfc` 52, `ladder` 31, `sfc` 26, `recipes` 16, `textlist` 16,
  `staticanalysis` 4, `iec6113110` 2, `OPC UA` 2.
* **A whole IEC object model is scriptable**: `create_program/function/function_block/gvl/dut/
  interface` plus `create_method/property/action`; a full FB with declaration text, a method body
  and a property still compiles with 0 errors.
* **Symbol configuration has a creation call after all**: `application.create_symbol_config(
  export_comments, opc_ua, client_side_layout_calculator)` — the calculator must be a real
  `System.Guid` (`Guid.Empty` works, `None` raises `TypeError`), and a second call on the same
  application is refused (`父对象不接受符号配置对象`). After a build the object reports
  `get_all_datatypes()` = 138 and `get_all_signatures()` = 69.
* **Project metadata unlocks libraries**: `project.get_project_info()` + title/version/**company**
  → `save_as_compiled_library` writes a 4 308 B `.compiled-library`. Without project info the
  engine says `指定的库不是托管库 (原因: 未发现工程信息/没有指定'公司')`.
* **Task timing is writable but string-typed**: `priority = 20` raises
  `TypeError: expected str, got int`; `"20"` works. Enabling a watchdog without a time breaks the
  build (`MainTask: 无效的看门狗时间`).
* **GUI-only commands are silent no-ops headless**: `导出IEC61131-10...`, `导出OPC UANodeSet`,
  `计算并导出标准指标`, `目标设置文档导出` all *execute without error*, write no file and emit no
  message — they open a dialog. `execute` success alone is therefore never evidence.
* **`save_as` leaves a claim behind**: the copy is complete and the project is renamed, but opening
  the new file immediately raises `所选工程当前正由 '<user>' 上的 '<machine>' 使用`; success is
  verified from the file and the renamed path instead.
* **Project comparison is not scriptable headless**: `compare_to` wants an
  `IExtendedObject[IScriptProject]` (a path raises `TypeError`) and opening a second project fails
  with `A primary project is already open`.
* **User management is readable but not writable as `(nobody)`**: `project.user_management` lists
  `Owner` / `Everyone`, while `users.create("tester")` is refused with
  `用户'(nobody)'未取得在'用户,组和权限'上操作'修改'的许可`.

## 4e. Third sweep: what is left, and why it cannot be scripted

Mined further (all live-verified): persistent variables, text-list **content** (ids + default +
per-language), command-permission audit, and a full **library round trip**
(`project.meta` → `export_library` 4 308 B → `install_library` with the repository argument,
available libraries 537 → 538).

Left, with the measured reason:

| area | why not |
| --- | --- |
| recipes, alarm configuration, visualizations, trace, application composer | no `create_*` entry exists in the 262 stub classes (`create_recipe*`, `create_alarm*`, `create_visualization*`, `create_trace*` are all absent) and the matching IDE commands open a dialog, so their objects cannot be created headless |
| static analysis, IEC 61131-10 export, OPC UA NodeSet, target-settings document | `execute` returns normally, writes no file and emits no message (dialog) |
| online file transfer / source upload | the simulated target reports `connected=false`; `get_file_list_of_directory` fails with `获取文件入口失败` |
| coredump, redundancy, breakpoints, watch list GUI | need a real PLC or an interactive debugger |
| CAS (Git/SVN) | the extension exists but needs a repository, credentials and a checked-out workdir — a separate project, not a one-shot probe |
| project comparison | `compare_to` needs a second *open* project; only one project can be primary |
| image pool content | `images.add` is overloaded/ambiguous and needs real image files |

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
