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

## 5. Timeouts

* Client socket timeout (`CodesysClient(timeout=…)`, default 60 s) is the hard one: on expiry the
  client raises `E_TIMEOUT` and drops the connection.
* `timeout_ms` in the request is **advisory**: the engine cannot be pre-empted mid-command, so the
  server compares elapsed time after the command finishes and answers `E_TIMEOUT` if it overran.
* `build` on a large project can take minutes; pass `timeout_ms`/`timeout` accordingly.

## 6. Security

* Binds `127.0.0.1` only; port is random by default (`--port 0`) and published in
  `service.json` together with a 32-hex token.
* Any local process that can read `service.json` can drive the IDE. Treat that file as a secret;
  `stop` removes it.
* `exec` (arbitrary IronPython inside CODESYS) is **off** unless the service is started with
  `--allow-exec`. It is an escape hatch, not an API.
