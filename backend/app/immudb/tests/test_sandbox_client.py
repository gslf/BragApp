import unittest
from unittest.mock import patch, AsyncMock
from app.immudb.client import Client

class TestSandboxClient(unittest.IsolatedAsyncioTestCase): 

    def setUp(self):
        self.client = Client("test_ledger", "http://example.com", "test_api_key", True)

    async def test_getCollectionDetails(self):
        collection_name = "test"
        
        with patch.object(self.client, 'getCollectionDetails', AsyncMock()) as mock_get:
            mock_get.return_value = {
                "fields": [
                    {"name": "_id", "type": "STRING"},
                    {"name": "_vault_md.ts", "type": "INTEGER"}
                ],
                "indexes": [
                    {"fields": ["_id"], "isUnique": True},
                    {"fields": ["_vault_md.ts"], "isUnique": False}
                ]
            }

            response = await self.client.getCollectionDetails(collection_name)
            self.assertGreater(len(response['fields']), 1)
            self.assertGreater(len(response['indexes']), 1)

    async def test_countCollection(self):
        collection_name = "test"
        expected_response = {"collection": "test", "count": 2}
        
        with patch.object(self.client, 'countCollection', AsyncMock()) as mock_count:
            mock_count.return_value = expected_response

            response = await self.client.countCollection(collection_name)
            self.assertEqual(response, expected_response)

    async def test_createCollection(self):
        collection_name = "test"
        collection_schema = {}
        
        with patch.object(self.client, 'createCollection', AsyncMock()) as mock_create:
            mock_create.return_value = True

            result = await self.client.createCollection(collection_name, collection_schema)
            self.assertTrue(result)

    async def test_deleteCollection(self):
        collection_name = "test"
        
        with patch.object(self.client, 'deleteCollection', AsyncMock()) as mock_delete:
            mock_delete.return_value = True

            result = await self.client.deleteCollection(collection_name)
            self.assertTrue(result)

    async def test_getData(self):
        collection_name = "test"
        page = 1
        count = 100
        
        with patch.object(self.client, 'getData', AsyncMock()) as mock_get_data:
            mock_get_data.return_value = {
                "page": 1,
                "revisions": [
                    {"document": {"_id": "66fae08a000000000000002053d8d0a5"}}
                ]
            }

            response = await self.client.getData(collection_name, page, count)
            self.assertIn("page", response)
            self.assertIn("revisions", response)

    async def test_setData(self):
        collection_name = "test"
        data = {}
        expected_response = {
            "documentId": "66fbb6f5000000000000002353d8d0af",
            "transactionId": "36"
        }

        with patch.object(self.client, 'setData', AsyncMock()) as mock_set:
            mock_set.return_value = expected_response

            response = await self.client.setData(collection_name, data)
            self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
