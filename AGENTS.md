# Notes for agents using codesyskit

## The only workflow that holds up

1. `codesyskit start` once, keep the process; `codesyskit status` proves it answers.
2. Do all work through **one** client session: `client.create(...)` →
   `client.write(...)` → `service.compile(client)` → `client.save()`.
3. Judge with read-backs: close the project, reopen it, read the text back. `readback_match` from
   `pou.write` is a hint, not proof.
4. Trust a green build only after you have seen a red one: run a garbage-write negative control
   whenever the build configuration changes.
5. `codesyskit stop` when done; the service keeps a CODESYS process alive (≈200 MB).

## Do not

* Do not create a project and immediately trust `build` — without a task configuration the
  compiler compiles nothing and prints `0错误,0警告`. Check `tasks` shows your POU.
* Do not use `client.call("exec", …)` in normal work; it is an escape hatch, off by default.
* Do not run two live tests (or two services on one state dir) at the same time.
* Do not parse the protocolled JSON by hand in shell scripts; use `codesyskit call`, which maps
  error codes to exit codes (2 unavailable, 3 timeout, 4 auth).
* Do not assume `system.get_messages()` reports compiler errors — read `Service.compile()`.

## Error codes you will actually meet

| code | what to do |
| --- | --- |
| `E_STATE` | no project/application, or a path segment is wrong — run `project.info` / `tree` |
| `E_ARGS` | wrong `part`, `kind`, `language`, or a missing `path` |
| `E_TIMEOUT` | raise `timeout`/`timeout_ms`; on a big project `build` needs minutes |
| `E_TOKEN` | `service.json` was replaced; read the state file again or restart |
| `E_UNAVAILABLE` | CODESYS missing, or `exec` without `--allow-exec` |

## Shape of a good session

```python
from codesyskit import Service

service = Service()
service.start()
client = service.client(timeout=300)
try:
    project = client.create(r"D:\\work\\job.project", device="CODESYS Control Win V3")
    pou = project["program"]
    client.write(pou, DECL, "declaration")
    client.write(pou, IMPL, "implementation")
    clean = service.compile(client)
    assert clean["ok"], clean["messages"][:3]
    assert client.call("tasks")["count"] == 1
    client.save()
finally:
    client.close()
    service.stop()
```
