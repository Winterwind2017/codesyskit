# Wire protocol (v1)

One JSON object per line, both directions, UTF-8. Loopback only.

```
request : {"v":1,"id":"<16 hex>","token":"<32 hex>","cmd":"ping","args":{},"timeout_ms":30000}
response: {"v":1,"id":"<same>","ok":true,"code":"OK","result":{…},"elapsed_ms":3}
error   : {"v":1,"id":"<same>","ok":false,"code":"E_STATE",
           "error":{"code":"E_STATE","message":"no project is open","detail":null},"elapsed_ms":1}
```

* `v` defaults to `1`; any other value ⇒ `E_PROTOCOL`.
* `token` must equal the one baked into the generated server script; mismatch ⇒ `E_TOKEN`
  (checked **before** the command is looked up).
* `args` must be an object; `timeout_ms` is advisory (see §5).
* Maximum request line: 1 MiB (`protocol.MAX_LINE`), enforced on both sides.
* The server answers **one request per connection** and closes it. That is deliberate: the script
  engine is single threaded, and a keep-alive connection would let one client starve the accept
  loop (measured: a second client timed out for 10 s while the first held an idle connection).

## 1. Error codes

| code | meaning | typical cause |
| --- | --- | --- |
| `OK` | success | — |
| `E_TOKEN` | auth failure | wrong/missing token |
| `E_PROTOCOL` | malformed request | bad JSON, wrong `v`, oversize line, closed socket |
| `E_TIMEOUT` | deadline exceeded | long command, or transport timeout on the client |
| `E_BUSY` | reserved | kept for a future concurrent dispatcher; not emitted today |
| `E_UNKNOWN_CMD` | no such command | typo, or a command from a newer kit |
| `E_ARGS` | bad/missing argument | missing `path`, unknown `kind`/`language`, bad `part` |
| `E_STATE` | wrong state | no project open, no active application, path segment missing |
| `E_UNAVAILABLE` | disabled or absent | `exec` without `--allow-exec`, CODESYS not installed |
| `E_SCRIPT` | exception inside the engine | .NET/IronPython error while executing the command |
| `E_CODESYS` | the engine reported a failure | reserved; compile failures are reported as data (`ok:false` inside `build`) |
| `E_INTERNAL` | kit bug | should never happen |

## 2. Commands

| cmd | args | result |
| --- | --- | --- |
| `ping` | — | `protocol`, `banner`, `ui_present`, `pid`, `uptime_s` |
| `version` | — | `banner`, `protocol`, `executable` |
| `devices` | `filter?`, `limit?` | `count`, `returned`, `items[{name,vendor,id,default_instance_name}]` |
| `projects` | — | `primary: {path,name,dirty} \| null` |
| `project.create` | `path`, `device?`, `device_node?`, `bare?`, `program?`, `task?`, `interval?`, `unit?`, `priority?` | `path`, `device`, `device_id`, `program`, `language`, `task` |
| `project.open` | `path` | `path`, `dirty` |
| `project.save` | `path?` (save-as) | `path`, `dirty` |
| `project.close` | — | `closed` |
| `project.info` | — | `path`, `dirty`, `application{name,path}`, `children[]` |
| `tree` | `path?`, `depth?` | `path`, `items[{name,path,type}]` |
| `pou.read` | `path`, `part` = `declaration\|implementation` | `text`, `length`, `linecount` |
| `pou.write` | `path`, `part`, `text` | `length`, `readback_match`, `readback` |
| `pou.create` | `name`, `kind` = `program\|function_block\|gvl\|dut`, `language?`, `parent?` | `path`, `name`, `kind`, `language` |
| `task.create` | `name?`, `pous?`, `interval?`, `unit?`, `priority?` | `task`, `path`, `pous` |
| `tasks` | — | `count`, `items[{name,path,kind,interval,pous[]}]` |
| `build` | — | `ok`, `errors`, `warnings`, `infos`, `count`, `items[]`, `cleared`, `build_ms` (server-side view; usually empty, see §4) |
| `messages` | `clear?` | same shape as `build` |
| `commands` | `filter?`, `limit?` | `count`, `returned`, `items[{name,guid,description,tokens}]` |
| `execute` | `name` \| `guid` \| `index` | `name`, `guid`, `elapsed_ms` |
| `object.info` | `path` | `name`, `path`, `is_folder`, `has_textual_declaration`, `has_textual_implementation`, `children[]` |
| `object.rename` | `path`, `name` | `path`, `name` |
| `object.delete` | `path` | `deleted` |
| `object.move` | `path`, `parent`, `index?` | `path`, `parent` |
| `folder.create` | `name`, `parent?` | `path`, `name` |
| `find.text` | `pattern`, `case_sensitive?`, `part?`, `limit?`, `path?` | `count`, `items[{path,part,line,text}]` |
| `libraries` | — | `referenced[]`, `referenced_count`, `available_count` |
| `library.add` | `name` | `added`, `referenced[]` |
| `export.xml` | `path`, `target?` | `path`, `exists`, `size` |
| `import.xml` | `path` | `path`, `children_before`, `children_after` |
| `export.native` | `path`, `target?` | `path`, `exists`, `size` |
| `project.archive` | `path` | `path`, `exists`, `size` |
| `generate.runtime` | `directory` | `directory`, `files[]` |
| `project.doc` | `path` | `E_UNAVAILABLE` in `--noUI` (measured no-op) |
| `online.simulation` | `enabled?` | `simulation`, `gateway`, `address` |
| `online.state` | — | `logged_in`, `simulation`, `gateway`, `address`, `application_state`, `operation_state` |
| `online.login` | `simulation?`, `change_option?` (`never`/`update`/`ask`), `delete_foreign?`, `autostart?` | snapshot (+ `start_error`) — or `E_CODESYS` |
| `online.logout` | — | `logged_in` |
| `online.start` | — | `started`, `application_state` |
| `online.stop` | — | `stopped`, `application_state` |
| `online.read` | `expression` \| `expressions[]` | `expression`+`value` or `values[]` |
| `online.write` | `expression`, `value` | `written`, `expression`, `value` |
| `online.download` | `simulation?` | snapshot + `boot_application` (login with `update` + create boot app) |
| `online.monitor` | `expression?`/`expressions[]`, `samples?`, `interval_ms?` | `samples[{index, <expr>: value}]`, `count`, `interval_ms` |
| `batch` | `calls[{cmd,args}]`, `stop_on_error?` | `results[{index,cmd,ok,code,result\|error}]`, `executed` |
| `exec` | `source` | `executed`, `locals` — **only** with `--allow-exec` |
| `quit` | — | `bye` |

`project.create` builds a compilable skeleton when `device` is given: an ST program (`PLC_PRG` by
default) plus a cyclic task (`MainTask`, 20 ms) that calls it. Pass `bare: true` to get the old
device-only project — see §3 for why that is almost never what you want.

## 3. Why the skeleton: the silent-compile trap

Measured on 3.5.22.20:

* project with device + POU, **no task configuration** → `build()` prints
  `编译完成 -- 0错误,0警告` **even when the POU contains `THIS IS NOT ST !!!`**;
* the same project after `application.create_task_configuration()` +
  `create_task("MainTask")` + `task.pous.add("PLC_PRG")` → `编译完成--12错误,2警告` with
  `C189 / C9 / C190` diagnostics.

Nothing is reachable from a task ⇒ nothing is compiled ⇒ "0 errors" is a lie. The kit therefore
creates the task in `project.create` and `Service.compile()` reports what the *engine log* says.

## 4. Where compile results actually come from

`system.get_messages()` and `get_message_objects()` return **0 items** even when the compiler
reports 12 errors — the diagnostics go to the process's stderr. The service therefore keeps the
engine's stderr in `engine.stderr.log`, and `Service.compile()` slices the bytes written during
the call and parses them:

```
编译: Error: C189: 应该用';' 替换'IS'
编译: Warning: C139: 代码'THIS;\n'不可能执行到.这是有目的的吗？
编译: Text: C0: 编译完成--12错误,2警告
```

`Text:` lines are progress chatter and are dropped; `Error/Warning/Fatal` become
`messages[{category,severity,code,text}]`; the `编译完成` summary is authoritative for counts.

## 4b. The IDE command channel (`commands` / `execute`)

`system.commands` exposes **870** IDE commands, each with `name`, `guid`, `description`,
`tokens` (e.g. `['project', 'rebuildactiveapp']`) and an `execute()` method. That is the
"anything the GUI can do" escape hatch without touching a window:

```python
service.run_command(client, "重新编译")     # judged from engine.stderr.log, like build
client.commands(filter="下载", limit=10)    # discover names first
client.execute(guid="50dc8f97-9e21-4b15-a504-ea2549ab61e0")
```

Names are localized (this install is Chinese); resolve by `guid` or `tokens` for stability.

## 4c. Exchange: XML / native / archive / runtime files

| what | call | measured result |
| --- | --- | --- |
| PLCopenXML of the application | `export.xml` (default target = active application) | 1 095 B for the demo app |
| PLCopenXML of a device subtree | `export.xml` with `target="/PLC"` | 1 988 B |
| re-import into an **empty** project | `import.xml` | children 2 → 3 |
| PLCopen native format | `export.native` | 23 091 B |
| whole-project archive | `project.archive` | 5 479 773 B |
| runtime system files | `generate.runtime` | `surfaceItf.m4` |
| documentation export | `project.doc` | **no file** — `export_doc` is a silent no-op headless |

The project root cannot be exported directly (`export_xml([project])` raises a cast error), which
is why the default target is the **active application**.

## 4d. Online: simulation is the headless path

The engine's online API needs a *target*. On this machine the CODESYS gateway and the soft PLC
are installed as **services** that a normal user cannot start (`sc start` → `Access is denied`;
the service DACL grants start only to SYSTEM/Administrators). That is **not** needed: the device
object has its own simulation flag, and simulation hosts the runtime inside the IDE process.

```python
client.online_simulation(True)        # device.set_simulation_mode(True) -> gateway auto-assigned
client.online_login(autostart=True)   # logged_in, application_state=run, operation_state=program_loaded
client.online_read("PLC_PRG.nCounter")        # "INT#8"
client.online_write("PLC_PRG.nCounter", "1000")
client.online_monitor(expression="PLC_PRG.nCounter", samples=5, interval_ms=300)
# samples: INT#1016, INT#1036, INT#1056, INT#1076, INT#1096   <- the cyclic task keeps running
client.online_stop()                  # application_state=stop
client.online_start()                 # application_state=run
client.online_download()              # login with change_option=update + create_boot_application
client.online_logout()
client.online_simulation(False)       # gateway back to 0000…, address ""
```

Measured facts behind the recipe:

| fact | value |
| --- | --- |
| simulation gateway | `164cdffe-053d-451a-ba6d-66afd90b25ac`, driver `SharedMemory` (`ShmBaseName=GWDrvSharedMemShm`) |
| device address after enabling simulation | `0000` (auto-assigned) |
| `set_gateway_and_address` address format | an IP string (`127.0.0.1` → normalised `0127.0000.0000.0001`); `"localhost"` / `"Gateway-1"` are rejected |
| login + `OnlineChangeOption.Never` | works in simulation, values keep running |
| `set_prepared_value` | needs a **string** value (`42` raises `TypeError: expected str, got int`) |
| boot application | `create_boot_application()` returns normally in simulation |

**One online application per project.** The server keeps the `OnlineApplication` alive
(`ONLINE` cache) and only logs in again when it is not logged in: a login is also an incremental
download, so re-logging in for every read restarts the program and resets every value to 0.

## 5. Timeouts

* Client socket timeout (`CodesysClient(timeout=…)`, default 60 s) is the hard one: on expiry the
  client raises `E_TIMEOUT` and drops the connection.
* `timeout_ms` in the request is **advisory**: the engine cannot be pre-empted mid-command, so the
  server compares elapsed time after the command finishes and answers `E_TIMEOUT` if it overran.
* `build` on a large project can take minutes; pass `timeout_ms`/`timeout` accordingly.

## 5c. Online states you will see

| field | values |
| --- | --- |
| `logged_in` | `true` / `false` |
| `application_state` | `none` (not logged in), `stop`, `run` |
| `operation_state` | `none`, `program_loaded`, … |
| `simulation` | `true` when the device simulation flag is on |
| `gateway` | GUID of the gateway used; `00000000-…` when none |
| `address` | device address (`0000` in simulation) |

## 5b. Text and paths

* **UTF-8 everywhere.** Replies are encoded with `Encoding.UTF8.GetBytes` and sent in a loop
  (`Socket.Send` may send a prefix); requests are accumulated as bytes and decoded as UTF-8.
  Before this was fixed, any reply containing Chinese raised
  `Cannot convert int(36333) to Byte` and the connection died. A live test writes
  `(* 中文注释：计数器 *)` and reads it back byte for byte.
* **Paths are name-based.** `/PLC/Plc Logic/Application/PLC_PRG`, built by walking the parent
  chain until the unnamed project root. Objects returned right after creation may not carry a
  name yet, so `folder.create` computes the path from the parent and re-resolves it.
* **The project root is immutable by design.** `object.rename`/`object.delete`/`object.move`
  refuse a path that resolves to the project (`E_STATE: refusing to modify the project root`).

## 6. Security

* Binds `127.0.0.1` only; port is random by default (`--port 0`) and published in
  `service.json` together with a 32-hex token.
* Any local process that can read `service.json` can drive the IDE. Treat that file as a secret;
  `stop` removes it.
* `exec` (arbitrary IronPython inside CODESYS) is **off** unless the service is started with
  `--allow-exec`. It is an escape hatch, not an API.
