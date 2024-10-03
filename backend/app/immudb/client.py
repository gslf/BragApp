from ._production_client import _ProductionClient
from ._sandbox_client import _SandboxClient
from ._api_client import _ApiClient

class Client:
    _instance: _ApiClient = None

    def __new__(cls, ledger: str, base_url: str, api_key: str, sandbox: bool = False) -> _ApiClient:

        if sandbox:
            cls._instance = _SandboxClient(ledger, base_url, api_key)
        else:
            cls._instance = _ProductionClient(ledger, base_url, api_key)

        return cls._instance