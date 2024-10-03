# app/utils/immudb_singleton.py

from fastapi import HTTPException
from app.adapters.immudb_adapter import ImmuDBAdapter

class ImmuDBAdapterSingleton:
    """
    Singleton class to ensure a single instance of ImmuDBAdapter is used.
    """
    _instance = None

    @classmethod
    async def get_instance(cls, sandbox, ledger, collection, base_url, api_key):
        if cls._instance is None:
            try:
                immudbAdapter = ImmuDBAdapter(
                    sandbox=sandbox,
                    ledger=ledger,
                    collection=collection,
                    base_url=base_url,
                    api_key=api_key
                )
                await immudbAdapter.connect()
                cls._instance = immudbAdapter
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        return cls._instance
