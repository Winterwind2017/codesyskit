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
