import asyncio
from typing import Any
from ._api_client import _ApiClient

class _SandboxClient(_ApiClient):
    """
    Concrete (sandboxed) implementation of the _ApiClient abstract base class.
    """

    def __init__(self, ledger: str, base_url: str, api_key: str):
        """Inherits docstring from _ApiClient."""
        super().__init__(ledger, base_url, api_key)

    async def getCollectionDetails(self, collection_name: str):
        """Inherits docstring from _ApiClient."""
        # Simulate a delay for asynchronous behavior
        await asyncio.sleep(0.1)

        # Standard account collection, with unique account_number
        response = {
            "fields": [
                {"name": "_id", "type": "STRING"},
                {"name": "_vault_md.ts", "type": "INTEGER"},
                {"name": "account_number", "type": "INTEGER"},
                {"name": "account_name", "type": "STRING"},
                {"name": "iban", "type": "STRING"},
                {"name": "address", "type": "STRING"},
                {"name": "amount", "type": "INTEGER"},
                {"name": "type", "type": "STRING"}
            ],
            "idFieldName": "_id",
            "indexes": [
                {"fields": ["_id"], "isUnique": True},
                {"fields": ["_vault_md.ts"], "isUnique": False},
                {"fields": ["account_number"], "isUnique": True}
            ],
            "name": "test"
        }
        return response

    async def countCollection(self, collection_name: str):
        """Inherits docstring from _ApiClient."""
        await asyncio.sleep(0.1)

        response = {"collection": "test", "count": 2}
        return response

    async def createCollection(self, collection_name: str, collection_schema: Any) -> bool:
        """Inherits docstring from _ApiClient."""
        await asyncio.sleep(0.1)
        return True

    async def deleteCollection(self, collection_name: str) -> bool:
        """Inherits docstring from _ApiClient."""
        await asyncio.sleep(0.1)
        return True

    async def getData(self, collection_name: str, page: int, count: int):
        """Inherits docstring from _ApiClient."""
        await asyncio.sleep(0.1)

        # Sample account records
        response = {
            "page": 1,
            "perPage": 100,
            "revisions": [
                {
                    "document": {
                        "_id": "66fae08a000000000000002053d8d0a5",
                        "_vault_md": {
                            "creator": "a:b595b399-3f5e-4a86-a76e-d1883b4fa3ee",
                            "ts": 1727717514
                        },
                        "account_name": "Test Name",
                        "account_number": 1234,
                        "address": "Test Address 2",
                        "amount": 10,
                        "iban": "IT123456978213456789",
                        "type": "sending"
                    },
                    "revision": "",
                    "transactionId": ""
                },
                {
                    "document": {
                        "_id": "66faee65000000000000002153d8d0a7",
                        "_vault_md": {
                            "creator": "a:b595b399-3f5e-4a86-a76e-d1883b4fa3ee",
                            "ts": 1727721061
                        },
                        "account_name": "Test Name",
                        "account_number": 12345,
                        "address": "Test Address 2",
                        "amount": 10,
                        "iban": "IT123456978213456789",
                        "type": "sending"
                    },
                    "revision": "",
                    "transactionId": ""
                }
            ],
            "searchId": ""
        }
        return response

    async def setData(self, collection_name: str, data: Any):
        """Inherits docstring from _ApiClient."""
        await asyncio.sleep(0.1)

        response = {"documentId": "66fbb6f5000000000000002353d8d0af", "transactionId": "36"}
        return response
