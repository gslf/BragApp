# app/api/operations_router.py

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.account import Account
from app.adapters.immudb_adapter import ImmuDBAdapter
from app.adapters.immudb_adapter_singleton import ImmuDBAdapterSingleton  
from app.settings import Settings

# Init the router
settings = Settings()
operations_router = APIRouter()

async def get_immudb_adapter():
    """
    Dependency to retrieve the singleton instance of ImmuDBAdapter.
    """
    return await ImmuDBAdapterSingleton.get_instance(
        sandbox=settings.IMMUDB_VAULT_SANDBOX,
        ledger=settings.IMMUDB_VAULT_LEDGER_NAME,
        collection=settings.IMMUDB_VAULT_COLLECTION_NAME,
        base_url=settings.IMMUDB_VAULT_BASEURL,
        api_key=settings.IMMUDB_VAULT_API_KEY
    )


@operations_router.get("/accounts/count",
                       summary="Get the number of accounts in the vault.",
                       response_model=int,
                       response_description="The total count of accounts in the vault collection.")
async def count_accounts(immudbAdapter: ImmuDBAdapter = Depends(get_immudb_adapter)):
    """
    Retrieve the total number of accounts in the vault.
    """
    result = await immudbAdapter.count_accounts()

    if result.status:
        return result.data
    else:
        raise HTTPException(status_code=result.code, detail=result.error)


@operations_router.get("/accounts/",
                       summary="Get a list of all account numbers in the vault.",
                       response_model=List[Account],
                       response_description="A list of all account numbers in the vault collection.")
async def get_accounts(page: int = 1, count: int = 10, immudbAdapter: ImmuDBAdapter = Depends(get_immudb_adapter)):
    """
    Retrieve a paginated list of accounts from the vault.
    """
    result = await immudbAdapter.get_accounts(page, count)

    if result.status:
        return result.data
    else:
        raise HTTPException(status_code=result.code, detail=result.error)


@operations_router.post("/accounts/",
                        summary="Add a new account transaction to the vault.",
                        response_model=str,
                        response_description="The Transaction ID")
async def set_account(account: Account, immudbAdapter: ImmuDBAdapter = Depends(get_immudb_adapter)):
    """
    Add a new account transaction to the vault.
    """
    result = await immudbAdapter.set_accounts(account)

    if result.status:
        return result.data
    else:
        raise HTTPException(status_code=result.code, detail=result.error)
