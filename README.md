# codesyskit

A resident, token-authenticated service for **CODESYS 3.5** (tested on 3.5.22.20) so an agent can
drive the IDE without the GUI and without registry changes.

```python
from codesyskit import Service

service = Service()
state = service.start()                     # headless CODESYS, ~7 s, random port
with service.client() as client:
    client.create(r"D:\work\demo.project", device="CODESYS Control Win V3")
    client.write("/PLC/Plc Logic/Application/PLC_PRG", "nCounter := nCounter + 1;\n", "implementation")
    print(service.compile(client))          # {"ok": True, "errors": 0, ...}
service.stop()
```

## Why a service and not COM

Measured on this machine, `ScriptEngine3.dll` (266 types, x86) has **no COM class to register**:

* `RegAsm /regfile` (dry run, no registry writes) yields **33 keys / 3 coclasses**, all of them
  `…HideFromScriptDocuAttribute`, `…IncludeIntoScriptDocuAttribute`, `…SyntaxErrorException`;
* `_3S.CoDeSys.ScriptEngine.IScriptEngine` is an **in-process managed interface name**, not a ProgID;
* `_3S.CoDeSys*` has **0 hits** in `HKCR`, `HKLM\SOFTWARE\Classes`, `HKCU\SOFTWARE\Classes`.

So the engine is hosted where it belongs — inside a headless CODESYS process — and the kit exposes
it over loopback. See `docs/ARCHITECTURE.md` for the full reasoning and `COM-vs-SERVER.md` in the
research notes for the comparison table.

## What you can drive

| area | commands |
| --- | --- |
| session | `ping` `version` `status` (service) |
| devices | `devices` (1 562 shipped descriptions, filter by name/vendor) |
| project | `project.create/open/save/close/info` `tree` `projects` |
| code | `pou.create/create_typed/read/write/member/members` `object.info/rename/delete/move` `folder.create` `find.text` |
| model | GVL / DUT / interface / FB / function, methods / properties / actions, persistent vars, `symbols.create`, `textlist.*` (rows + per-language texts) |
| project | `project.meta` `project.save_as` `project.export_library` `project.clean` `project.users` `project.integrity` `project.io_export/import` |
| app | `app.clean` `app.generate` `app.status` |
| tasks | `task.info` `task.update` (priority / interval / watchdog) |
| tasks | `task.create` `tasks` |
| build | `build` (judged from the engine log) |
| IDE commands | `commands` (870) `execute` |
| libraries | `libraries` (537 available) `library.add` `library.install` (537 → 538) |
| exchange | `export.xml` `import.xml` `export.native` `project.archive` `generate.runtime` |
| online | `online.simulation` `online.state/login/logout/start/stop/read/write/monitor/download` — **simulation runs headless, no gateway, no admin** |

## Verified behaviour

Live end-to-end (`python tests/live_service.py`, 16/16):

| step | result |
| --- | --- |
| `service.start` | 7.3 s, `ui_present=False`, random port |
| `ping` | 0.00 s |
| `devices` | 1562 device descriptions |
| `project.create(device=…)` | creates project + ST POU + cyclic task (3.6 s) |
| `pou.write` | readback matches |
| `compile(valid)` | **0 errors** |
| `compile("THIS IS NOT ST !!!")` | **12 errors, 2 warnings**, codes `C189/C139/C9/C190` |
| `reopen + read back` | text survives save/reopen |
| bare project (no task) | **compiles nothing, 0 errors** — the trap this kit warns about |
| bad token / unknown command | `E_TOKEN` / `E_UNKNOWN_CMD` |
| `service.stop` | 1.2 s |

Extended surface (`python tests/live_surface.py`, 22/22):

| step | result |
| --- | --- |
| `commands` | 870 IDE commands with guid/tokens/description |
| `execute 重新编译` | judged from the engine log, 0 errors |
| move / rename / delete round trip | restored to the original path |
| UTF-8 text round trip | `(* 中文注释：计数器 *)` read back byte for byte |
| `find.text` | 3 hits with line numbers |
| `libraries` | 4 referenced, 537 available; `library.add("Standard")` sticks |
| `export.xml` | 1 095 B (app) / 1 988 B (device subtree) |
| `import.xml` | empty project children 2 → 3 |
| `export.native` / `project.archive` / `generate.runtime` | 23 KB / 5.4 MB / `surfaceItf.m4` |
| `project.doc` | honest `E_UNAVAILABLE` (silent no-op headless) |
| `online.state` / `online.login` | `logged_in:false` / `E_CODESYS` with the gateway message |

Deep surface (`python tests/live_deep.py`, 36/36):

| step | result |
| --- | --- |
| `pou.create_typed` × 5 | GVL, DUT, interface, function block, function (INT) — all created, text written |
| `pou.member` × 3 | method / property / action under `FB_Motor`, 3 members listed |
| compile after all that | 0 errors |
| `task.info` / `task.update` | priority `1 → 20`, interval `20 → 10` ms |
| `symbols.create` | symbol configuration created; after a build 138 datatypes / 69 signatures |
| `textlist.*` | zh-CN + en + fr, `export` writes 238 B |
| `project.meta` + `export_library` | 4 308 B compiled library (needs title **and** company) |
| `project.save_as` | copy becomes primary, verified from file + renamed path |
| `project.io_export` | 235 B I/O mapping CSV |
| `project.users` / `project.integrity` | users/groups listed (creation refused as `(nobody)`); integrity check `false → true` |
| `app.clean` / `app.generate` / `app.status` | `is_uptodate` false → true, online change possible |
| `online.force(777)` | value pinned at 777 while the task runs; `unforce` resumes 790 → 888 |
| `textlist.rows` / `textlist.text` | id `0000-0000-{…}-Version`, default text written, zh-CN added, export 268 B |
| `project.permissions` | `仿真` → Owner `true`, Everyone `true`, guid `515e05ec-…` |
| `library.install` | our own compiled library installed: available libraries **537 → 538** |
| `online.files` | honest `E_UNAVAILABLE` (simulated target reports `connected=false`) |

Online through **simulation** (`python tests/live_online.py`, 16/16):

| step | result |
| --- | --- |
| `online.simulation(True)` | gateway auto-assigned (`164cdffe-…`, driver `SharedMemory`), address `0000` |
| `online.login(autostart=True)` | `logged_in:true`, `application_state=run`, `operation_state=program_loaded` |
| cyclic task really runs | `nCounter` 8 → 68 within 1.2 s |
| `online.write(1000)` | readback 1007 |
| `online.monitor(5 × 300 ms)` | 1016 → 1036 → 1056 → 1076 → 1096 |
| `online.stop` / `online.start` | `stop` / `run` |
| `online.download` | login with `update` + `create_boot_application` → True |
| `online.logout` + `simulation(False)` | logged out; gateway back to `0000…`, address `""` |
| login without gateway | honest `E_CODESYS` |

## Install

```powershell
py -m pip install -e D:\bililive\codesyskit
# or run from the tree:
$env:PYTHONPATH = "D:\bililive\codesyskit\src"
python -m codesyskit start
```

Defaults: `--exe "D:\Program Files\CODESYS 3.5.22.20\CODESYS\Common\CODESYS.exe"`,
`--profile "CODESYS V3.5 SP22 Patch 2"`; override with `--exe/--profile` or `CODESYSKIT_EXE` /
`CODESYSKIT_PROFILE`. State (`service.json` with port+token, generated `server.py`, `service.log`,
`engine.stderr.log`) lives in `%LOCALAPPDATA%\codesyskit` unless `--state-dir` says otherwise.

## CLI

```
codesyskit start [--port 0] [--allow-exec] [--wait 180]
codesyskit status
codesyskit ping
codesyskit devices --filter "Control Win" --limit 5
codesyskit call build --args '{}' --timeout 600
codesyskit batch --file calls.json
codesyskit commands --filter 编译      # 870 IDE commands
codesyskit execute 重新编译            # run one, judged from the engine log
codesyskit find nCounter              # search declarations + implementations
codesyskit libs                       # referenced / available libraries
codesyskit export-xml out.xml         # PLCopenXML of the active application
codesyskit archive job.projectarchive
codesyskit sim                     # enable device simulation (no gateway needed)
codesyskit online-login --autostart
codesyskit online-monitor PLC_PRG.nCounter --samples 5 --interval-ms 300
codesyskit online-write PLC_PRG.nCounter 1000
codesyskit online-stop
codesyskit run script.py              # one-shot --runscript, no resident process
codesyskit server-script [--out f]    # print the generated IronPython server
codesyskit stop
```

Exit codes: `0` ok, `1` error, `2` unavailable, `3` timeout, `4` auth.

## Layout

```
src/codesyskit/   errors.py protocol.py agentscript.py client.py service.py cli.py
tests/            protocol/client/agentscript/engine-log unit tests + fake_server.py + live_service.py
docs/             PROTOCOL.md ARCHITECTURE.md VERIFY.md UNSUPPORTED.md
tools/selfcheck.py
```

## Gates

```powershell
python -m pytest tests -q      # 31 tests, no CODESYS needed
python tools\selfcheck.py
python tests\live_service.py   # needs CODESYS; skips cleanly otherwise
```

## Licence

MIT.
