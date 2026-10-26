"""codesyskit -- resident, token-authenticated service for CODESYS 3.5 scripting.

The CODESYS script engine is an in-process .NET plugin with no COM class to register
(measured: ``RegAsm /regfile`` yields only attribute/exception coclasses), so the kit runs the
engine *inside* a headless CODESYS process and exposes a small JSON protocol over loopback.

    from codesyskit import Service
    service = Service()
    state = service.start()          # {"port": 5xxxx, "token": "...", "pid": ...}
    with service.client() as client:
        print(client.ping())
        print(client.devices(limit=3))
    service.stop()
"""

from .client import CodesysClient
from .protocol import ServiceError
from .service import Service

__all__ = ["CodesysClient", "Service", "ServiceError"]
__version__ = "0.1.0"
