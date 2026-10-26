"""Stable error codes for the CODESYS resident service.

Every response carries exactly one of these.  ``ok`` is true only for ``OK``.
The set is closed: adding a code means bumping :data:`PROTOCOL_VERSION`.
"""

OK = "OK"

# transport / auth
E_TOKEN = "E_TOKEN"              # missing or wrong token
E_PROTOCOL = "E_PROTOCOL"        # unparsable request, wrong version, oversize line
E_TIMEOUT = "E_TIMEOUT"          # the command exceeded its deadline
E_BUSY = "E_BUSY"                # a command is already running (single-threaded engine)

# dispatch
E_UNKNOWN_CMD = "E_UNKNOWN_CMD"
E_ARGS = "E_ARGS"                # missing/invalid argument
E_STATE = "E_STATE"              # no project open, no active application, bad path
E_UNAVAILABLE = "E_UNAVAILABLE"  # feature disabled (e.g. exec) or not supported here

# execution
E_SCRIPT = "E_SCRIPT"            # IronPython/.NET exception raised by the command
E_CODESYS = "E_CODESYS"          # the engine returned a failure (e.g. build failed)
E_INTERNAL = "E_INTERNAL"        # server-side bug; never expected

ALL = (
    OK, E_TOKEN, E_PROTOCOL, E_TIMEOUT, E_BUSY, E_UNKNOWN_CMD, E_ARGS, E_STATE,
    E_UNAVAILABLE, E_SCRIPT, E_CODESYS, E_INTERNAL,
)

# exit codes of the CLI, so scripts can branch without parsing JSON
CLI_OK = 0
CLI_ERROR = 1
CLI_UNAVAILABLE = 2
CLI_TIMEOUT = 3
CLI_AUTH = 4
