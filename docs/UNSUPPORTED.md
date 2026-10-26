# Not done (and why)

| area | status | reason |
| --- | --- | --- |
| COM registration of the engine | **not possible** | `RegAsm /regfile` on `ScriptEngine3.dll` yields only 3 attribute/exception coclasses; `_3S.CoDeSys*` has 0 registry hits. See `docs/ARCHITECTURE.md` §1. |
| online: login / download / run-stop / monitoring | not implemented | `ScriptOnline` has 19 classes / 112 methods, but it needs a reachable PLC or the local soft PLC; the kit stops at offline build until that is set up and measured. |
| trace / visualization configuration | not implemented | `ScriptTraceObject`, `ScriptImagePoolObject`, … exist; no verified recipe yet. |
| library and package management | not implemented | `LibManager` (74 methods) and `PackageManagerCLI.exe` are available; version pinning on customer projects is a separate problem. |
| project archive / XML exchange | not implemented | `save_archive` / `export_xml` / `import_xml` exist; the kit prefers object-level edits for now. |
| GUI automation | **deliberately absent** | the engine is scriptable headless; driving windows would be strictly worse. |
| concurrent clients | not supported | the engine is single threaded; use one client or a queue in front of the service. |
| `exec` | off by default | arbitrary IronPython inside the IDE; enabled only with `--allow-exec`. |

## Known sharp edges

* A project without a task configuration compiles nothing and reports **0 errors** — always check
  `tasks` before trusting a green build.
* `system.get_messages()` stays empty even when the compiler fails; diagnostics are on stderr.
* `ScriptDeviceCollection` is not subscriptable; wrap in `list()`.
* The engine's stderr is UTF-8; decoding it as the ANSI codepage produces mojibake.
* Starting the service costs ~7 s; batch calls instead of starting per action.
