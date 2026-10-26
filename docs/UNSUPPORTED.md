# Not done (and why)

| area | status | reason |
| --- | --- | --- |
| COM registration of the engine | **not possible** | `RegAsm /regfile` on `ScriptEngine3.dll` yields only 3 attribute/exception coclasses; `_3S.CoDeSys*` has 0 registry hits. See `docs/ARCHITECTURE.md` §1. |
| online: login / download / run-stop / monitoring | **implemented, blocked by the environment** | the commands exist and their failure path is verified: `online.state` → `logged_in:false`, `online.login` → `E_CODESYS` with `网关没有正确配置`. The CODESYS Gateway V3 and CODESYS Control Win V3 - x64 are installed as services, both `Stopped`, `StartMode=Manual`; starting them needs elevation, and running `GatewayService.exe` / `CODESYSControlService.exe` as a user process exits immediately (measured). |
| trace / visualization configuration | not implemented | `ScriptTraceObject`, `ScriptImagePoolObject`, … exist; no verified recipe yet. |
| library and package management | not implemented | `LibManager` (74 methods) and `PackageManagerCLI.exe` are available; version pinning on customer projects is a separate problem. |
| project archive / XML exchange | **done** | `export.xml` (1 095 B app / 1 988 B device subtree), `import.xml` (empty project 2 → 3 children), `export.native` (23 KB), `project.archive` (5.4 MB), `generate.runtime` (`surfaceItf.m4`) — all live-verified. |
| symbol configuration creation | not available in this version | no `create_symbol_configuration` on application or device (`AttributeError`); existing symbol configs can only be inspected. |
| documentation export (`project.doc`) | silent no-op headless | `export_doc` returns normally and writes nothing; the command answers `E_UNAVAILABLE` rather than pretending. |
| compiled-library export | not implemented | `save_as_compiled_library` needs project info ("指定的库不是托管库 / 未发现工程信息"). |
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
