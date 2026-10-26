# Not done (and why)

| area | status | reason |
| --- | --- | --- |
| COM registration of the engine | **not possible** | `RegAsm /regfile` on `ScriptEngine3.dll` yields only 3 attribute/exception coclasses; `_3S.CoDeSys*` has 0 registry hits. See `docs/ARCHITECTURE.md` §1. |
| online against a **real PLC** through the gateway | not verified | the gateway/PLC services exist but only SYSTEM/Administrators may start them (`sc start` → `Access is denied`; DACL `(A;;CCLCSWLOCRRC;;;IU)` has no start right), and the service binaries exit when launched as a plain process. Everything above that layer is implemented and tested — point the device at a running gateway and the same commands apply. |
| trace / visualization configuration | not implemented | `ScriptTraceObject`, `ScriptImagePoolObject`, … exist; no verified recipe yet. |
| library and package management | not implemented | `LibManager` (74 methods) and `PackageManagerCLI.exe` are available; version pinning on customer projects is a separate problem. |
| project archive / XML exchange | **done** | `export.xml` (1 095 B app / 1 988 B device subtree), `import.xml` (empty project 2 → 3 children), `export.native` (23 KB), `project.archive` (5.4 MB), `generate.runtime` (`surfaceItf.m4`) — all live-verified. |
| symbol configuration creation | not available in this version | no `create_symbol_configuration` on application or device (`AttributeError`); existing symbol configs can only be inspected. |
| documentation export (`project.doc`) | silent no-op headless | `export_doc` returns normally and writes nothing; the command answers `E_UNAVAILABLE` rather than pretending. |
| compiled-library export | not implemented | `save_as_compiled_library` needs project info ("指定的库不是托管库 / 未发现工程信息"). |
| GUI automation | **deliberately absent** | the engine is scriptable headless; driving windows would be strictly worse. |
| concurrent clients | not supported | the engine is single threaded; use one client or a queue in front of the service. |
| `exec` | off by default | arbitrary IronPython inside the IDE; enabled only with `--allow-exec`. |

## Online: what *is* verified

`tests/live_online.py` (16/16) proves the whole chain in **simulation** (no gateway, no PLC, no
admin): `set_simulation_mode(True)` → login → `application_state=run` → the cyclic task increments
`nCounter` (8 → 68) → `write 1000` → readback 1007 → `monitor` 5 samples (1016…1096) → `stop`
→ `start` → `download` creates a boot application → `logout` → `simulation(False)` clears the
gateway and a login then fails with `E_CODESYS`.

## Known sharp edges

* A project without a task configuration compiles nothing and reports **0 errors** — always check
  `tasks` before trusting a green build.
* `system.get_messages()` stays empty even when the compiler fails; diagnostics are on stderr.
* `ScriptDeviceCollection` is not subscriptable; wrap in `list()`.
* The engine's stderr is UTF-8; decoding it as the ANSI codepage produces mojibake.
* Starting the service costs ~7 s; batch calls instead of starting per action.
