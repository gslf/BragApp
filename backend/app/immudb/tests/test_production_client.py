import unittest
from unittest.mock import patch, ANY, AsyncMock, MagicMock
from app.immudb.client import Client

class TestProductionClient(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client("test_ledger", "http://example.com", "test_api_key", False)

    @patch('httpx.AsyncClient.request', new_callable=AsyncMock)
    async def test_getCollectionDetails(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        collection_name = "test"
        response = await self.client.getCollectionDetails(collection_name)

        mock_request.assert_called_once_with(
            "GET",
            f"http://example.com/ledger/test_ledger/collection/{collection_name}",
            params=None,
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },            
            cookies=None,
            auth=ANY,  
            follow_redirects=ANY,
            timeout=ANY,
            extensions=None
        )

    @patch('httpx.AsyncClient.post', new_callable=AsyncMock)
    async def test_countCollection(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        collection_name = "test"
        response = await self.client.countCollection(collection_name)

        mock_post.assert_called_once_with(
            f"http://example.com/ledger/test_ledger/collection/{collection_name}/documents/count",
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },
            json={}
        )

    @patch('httpx.AsyncClient.request', new_callable=AsyncMock)
    async def test_createCollection(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        collection_name = "test"
        collection_schema = {"schema": "example"}
        result = await self.client.createCollection(collection_name, collection_schema)

        mock_request.assert_called_once_with(
            "PUT",
            f"http://example.com/ledger/test_ledger/collection/{collection_name}",
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },
            json=collection_schema,
            content=None,
            data=None,
            files=None,
            params=None,
            cookies=None,
            auth=ANY,  
            follow_redirects=ANY,
            timeout=ANY,
            extensions=None
        )

    @patch('httpx.AsyncClient.request', new_callable=AsyncMock)
    async def test_deleteCollection(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        collection_name = "test"
        result = await self.client.deleteCollection(collection_name)

        mock_request.assert_called_once_with(
            "DELETE",
            f"http://example.com/ledger/test_ledger/collection/{collection_name}",
            params=None,
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },
            cookies=None,
            auth=ANY, 
            follow_redirects=ANY, 
            timeout=ANY, 
            extensions=None
        )

    @patch('httpx.AsyncClient.request', new_callable=AsyncMock)
    async def test_getData(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        collection_name = "test"
        page = 1
        count = 100
        response = await self.client.getData(collection_name, page, count)

        mock_request.assert_called_once_with(
            "POST",
            f"http://example.com/ledger/test_ledger/collection/{collection_name}/documents/search",
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },
            json=ANY,
            content=None,
            data=None,
            files=None,
            params=None,
            cookies=None,
            auth=ANY,  
            follow_redirects=ANY,
            timeout=ANY,
            extensions=None
        )

    @patch('httpx.AsyncClient.request', new_callable=AsyncMock)
    async def test_setData(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        collection_name = "test"
        data = {"data": "example"}
        response = await self.client.setData(collection_name, data)

        mock_request.assert_called_once_with(
            "PUT",
            "http://example.com/ledger/test_ledger/collection/test/document",
            params=None,
            headers={
                'accept': 'application/json',
                'X-API-Key': 'test_api_key',
                'Content-Type': 'application/json'
            },
            json=ANY,
            content=None,
            data=None,
            files=None,
            cookies=None,
            auth=ANY,  
            follow_redirects=ANY,
            timeout=ANY,
            extensions=None
        )

if __name__ == '__main__':
    unittest.main()
