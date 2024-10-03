import httpx
import json
from typing import Any, Dict
from ._api_client import _ApiClient

class _ProductionClient(_ApiClient):
    """
    Concrete implementation of the _ApiClient abstract base class.
    """

    def __init__(self, ledger: str, base_url: str, api_key: str):
        """Inherits docstring from _ApiClient."""
        super().__init__(ledger, base_url, api_key)

    async def getCollectionDetails(self, collection_name: str):
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}"
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise response.raise_for_status()

    async def countCollection(self, collection_name: str):
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}/documents/count"
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json={})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def createCollection(self, collection_name: str, collection_schema: Any) -> bool:
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}"
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, json=collection_schema)

        if response.status_code == 200:
            return True
        else:
            response.raise_for_status()

    async def deleteCollection(self, collection_name: str) -> bool:
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}"
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            response.raise_for_status()

    async def getData(self, collection_name: str, page: int, count: int):
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}/documents/search"
        payload = {
            "page": page,
            "perPage": count
        }
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def setData(self, collection_name: str, data: Dict):
        """Inherits docstring from _ApiClient."""
        url = f"{self.base_url}/ledger/{self.ledger}/collection/{collection_name}/document"
        headers = {
            'accept': 'application/json',
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
