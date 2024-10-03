from pydantic import BaseModel, Field
from app.schemas.operation_type import OperationType

account_schema = {
    "fields":[
         {
            "name": "account_number",
            "type": "INTEGER"
        },
        {
            "name": "account_name",
            "type": "STRING"
        },
        {
            "name": "iban",
            "type": "STRING"
        },
        {
            "name": "address",
            "type": "STRING"
        },
        {
            "name": "amount",
            "type": "INTEGER"
        },
        {
            "name": "type",
            "type": "STRING"
        }
    ],
    "indexes": [
        {
            "fields": ["account_number"],
            "isUnique": True
        }
    ]
}

class Account(BaseModel):
    """
    Represents a bank account with associated details.

    Attributes:
        account_number (int): Unique account number.
        account_name (str): Name associated with the account.
        iban (str): Valid IBAN number associated with the account.
        address (str): Address associated with the account.
        amount (float): Amount of money in the account.
        type (OperationType): Type of account (sending or receiving).
    """
    
    account_number: int = Field(..., description="Unique account number")
    account_name: str = Field(..., min_length=1, max_length=100, description="Name associated with the account")
    iban:  str = Field(..., pattern=r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$', description="Valid IBAN number")
    address: str = Field(..., min_length=1, max_length=200, description="Address associated with the account")
    amount: float = Field(..., ge=1, description="Amount of money in the account")
    type: OperationType = Field(..., description="Type of account: sending or receiving")



    

