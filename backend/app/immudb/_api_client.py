from typing import Any, Dict, Optional, List
from abc import ABC, abstractmethod

class _ApiClient(ABC):
    """
    Abstract base class for an API client interacting with a specific ledger system.

    This class provides an interface for performing CRUD operations on collections and
    interacting with their data. Implementations of this class should provide the actual
    HTTP request logic for the defined methods.

    Attributes:
        ledger (str): The name of the ledger associated with the client.
        base_url (str): The base URL of the API.
        api_key (str): The API key used for authentication.
    """

    def __init__(self, ledger: str, base_url: str, api_key: str):
        """
        Initializes the API client with the ledger, base URL, and API key.

        Args:
            ledger (str): The name of the ledger.
            base_url (str): The base URL of the API.
            api_key (str): The API key for authenticating requests.
        """
        self.ledger = ledger
        self.base_url = base_url
        self.api_key = api_key

    @abstractmethod
    async def getCollectionDetails(self, collection_name: str):
        """
        Retrieve details about a specific collection.

        Args:
            collection_name (str): The name of the collection to retrieve details for.

        Returns:
            Any: The details of the collection. The exact structure of the returned
            data depends on the API implementation.
        """
        pass

    @abstractmethod
    async def countCollection(self, collection_name: str):
        """
        Count the number of items in a specific collection.

        Args:
            collection_name (str): The name of the collection to count items for.

        Returns:
            Any: The count of items in the collection. The return type depends on the
            API implementation.
        """
        pass

    @abstractmethod
    async def createCollection(self, collection_name: str, collection_schema: Any) -> bool:
        """
        Create a new collection with the specified schema.

        Args:
            collection_name (str): The name of the collection to create.
            collection_schema (Any): The schema for the new collection.

        Returns:
            bool: True if the collection was created successfully, False otherwise.
        """
        pass

    @abstractmethod
    async def deleteCollection(self, collection_name: str) -> bool:
        """
        Delete an existing collection.

        Args:
            collection_name (str): The name of the collection to delete.

        Returns:
            bool: True if the collection was deleted successfully, False otherwise.
        """
        pass

    @abstractmethod
    async def getData(self, collection_name: str, page:int, count: int):
        """
        Retrieve data from a collection, paginated by page and count.

        Args:
            collection_name (str): The name of the collection to retrieve data from.
            page (int): The page number of the data to retrieve.
            count (int): The number of items to retrieve per page.

        Returns:
            Any: The retrieved data. The structure of the returned data depends on the
            API implementation.
        """
        pass

    @abstractmethod
    async def setData(self, collection_name: str, data: Any):
        """
        Insert or update data in a specific collection.

        Args:
            collection_name (str): The name of the collection to insert or update data in.
            data (Any): The data to insert or update.

        Returns:
            Any: The result of the operation. The return type depends on the API
            implementation.
        """
        pass