# How results are judged

Rule zero: **a return value is not evidence**. Every claim in this kit is backed by a read-back,
an engine-produced artefact, or a negative control (a case that must fail).

## 1. Code text: reopen and compare

```python
client.write(path, text, "implementation")
client.call("project.close")
client.open(project_path)                     # a different project instance
assert client.read(path, "implementation")["text"] == text
```

`pou.write` already returns `readback_match`, but the authoritative check is the reopen: it proves
the text reached the project file, not just the in-memory document.

## 2. Compilation: the engine log, plus a negative control

`Service.compile(client)`:

1. records the byte offset of `engine.stderr.log`;
2. calls `build` through the service;
3. slices the log written during that call;
4. keeps `Error/Warning/Fatal` lines (drops `Text:` chatter) and takes the
   `编译完成--N错误,M警告` summary as the count.

A bare "0 errors" is only trusted together with a **negative control**: write
`THIS IS NOT ST !!!` and require `errors > 0` and at least one `C*` code. The live test does
exactly this (`compile(garbage) -> errors > 0`, observed 12 errors / codes `C189,C139,C9`).

## 3. The silent-compile trap must stay visible

`tests/live_service.py` builds a **bare** project (device only, no task configuration), writes
garbage, and asserts the compiler says **0 errors**. That assertion is intentional: it documents
that a task-less project compiles nothing, and it fails loudly if a future CODESYS starts
behaving differently. `docs/PROTOCOL.md` §3 explains the fix (task + `task.pous.add`).

## 4. Protocol behaviour: error codes, not strings

* wrong token ⇒ `E_TOKEN` (asserted live and in `tests/test_client.py`);
* unknown command ⇒ `E_UNKNOWN_CMD`;
* missing argument ⇒ `E_ARGS`;
* exception inside the engine ⇒ `E_SCRIPT` with a traceback in `detail`;
* client-side timeout ⇒ `E_TIMEOUT` (asserted against a deliberately slow fake server);
* batch keeps per-call codes, so a partial failure is never flattened into one boolean.

## 5. Gates

| gate | command | expectation |
| --- | --- | --- |
| unit | `python -m pytest tests -q` | 31 passed, no CODESYS needed |
| self-check | `python tools\selfcheck.py` | imports, verbs, docs, protocol constants |
| live | `python tests\live_service.py` | 16/16 passed, or `[SKIP]` without CODESYS |

Never run the live test twice in parallel: two headless IDEs will fight over the same project path
and the same profile.
