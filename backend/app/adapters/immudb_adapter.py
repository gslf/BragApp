import httpx
from app.schemas.account import Account, account_schema
from app.immudb.client import Client
from .immudb_adapter_response import ImmuDBAdapterResponse

class ImmuDBAdapter():
    """
    Adapter for interacting with an ImmuDB instance to perform account-related operations.

    This class provides methods to count, retrieve, and set account data in a specific 
    collection within an ImmuDB ledger.
    """

    def __init__(self, sandbox: bool, ledger: str, collection: str, base_url: str, api_key: str):
        """
        Initialize the ImmuDBAdapter with the provided configuration.

        Depending on the `sandbox` flag, the adapter connects to either the sandbox environment
        or the production environment of the ImmuDB instance.

        Args:
            sandbox (bool): Whether to use the sandbox environment.
            ledger (str): The name of the ledger to connect to.
            collection (str): The name of the collection within the ledger.
            base_url (str): The base URL of the ImmuDB instance.
            api_key (str): The API key for authenticating requests.
        """

        self.sandbox = sandbox
        self.ledger = ledger
        self.collection_name = collection
        self.base_url = base_url
        self.api_key = api_key
        self.client = None

    async def connect(self):
        if self.sandbox:
            self.client = Client(
                "test_ledger", 
                "http://example.com", 
                "test_api_key", 
                True
            )

        else:
            self.client = Client(
                self.ledger,
                self.base_url,
                self.api_key,
                False
            )

            await self._check_or_create_collection()

    # ================================
    #  INIT VAULT SECTION
    # ================================

    async def _check_or_create_collection(self):
        """
        Check if the collection exists in the ledger and has the correct schema. 
        If not, attempt to create it.

        Raises:
            ConnectionError: If the collection cannot be accessed, the schema is incorrect, 
            or the collection cannot be created due to issues such as missing fields or schema mismatches.
        """
        try:
            await self._check_collection_schema()

        except httpx.HTTPStatusError as http_err:
            if http_err.response.status_code == 404:
                await self._create_collection()
            else:
                raise ConnectionError(
                    f"Collection {self.collection_name} is not available in the vault."
                )

        except Exception as e:
            raise ConnectionError(f"The vault is not available. {str(e)}")


    async def _check_collection_schema(self):
        """Checks if the collection exists and its schema is valid."""
        response = await self.client.getCollectionDetails(self.collection_name)
        
        missing_fields, type_mismatches, account_number_unique = self._verify_fields(response, account_schema)

        if missing_fields:
            raise ConnectionError(f"Collection schema error: missing fields: {missing_fields}")
        if type_mismatches:
            raise ConnectionError(f"Collection schema error: type mismatches: {type_mismatches}")
        if not account_number_unique:
            raise ConnectionError("Collection schema error: the field account_number is not unique.")


    async def _create_collection(self):
        """Attempts to create the collection if it does not exist."""
        try:
            creation_result = await self.client.createCollection(self.collection_name, account_schema)
            
            if not creation_result:
                raise ConnectionError(f"Failed to create the collection in the vault.")

        except httpx.HTTPStatusError as http_err:
            if http_err.response.status_code == 402:
                raise ConnectionError("Collection creation requires a payment.")
            else:
                raise ConnectionError(f"Failed to create the collection in the vault. {http_err.response.status_code}")

        except Exception:
            raise ConnectionError("The vault is not available.")

    def _verify_fields(self, json_data, model):
        """
        Verify the fields in the collection schema against the expected fields in the model.

        Args:
            json_data (dict): The collection schema data from the vault.
            model (BaseModel): The Pydantic model to compare against the schema.

        Returns:
            tuple: A tuple containing three elements:
                - missing_fields (list): A list of fields missing from the collection schema.
                - type_mismatches (list): A list of fields where the types in the schema do not match the model.
                - account_number_unique (bool): Whether the account_number field is marked as unique in the schema.
        """
        
        model_fields = model['fields']
        json_fields = json_data['fields']

        missing_fields = []
        type_mismatches = []
        
        # Check if collection contain all fields with the right type
        for field in model_fields:
            field_name = field['name']
            field_type = field['type']

            matching_item = next((item for item in json_fields if item['name'] == field_name), None)
            if matching_item:
                if field_type != matching_item['type']:
                    type_mismatches.append(f"Field {field_name} type mismatch: {field_type} != {matching_item['type']}")
            else:
                missing_fields.append(field_name)
        
        # Check if account_number is unique
        account_number_unique = any(
            idx['fields'] == ['account_number'] and idx['isUnique'] for idx in json_data['indexes']
        )

        return missing_fields, type_mismatches, account_number_unique

    # ================================
    #  API call section
    # ================================
    async def count_accounts(self) -> ImmuDBAdapterResponse:
        """
        Count the number of accounts in the collection.

        Returns:
            ImmuDBAdapterResponse: A response object containing the account count
            or an error message in case of failure.
        """
        try:
            count_data = await self.client.countCollection(self.collection_name)
            
            if 'count' in count_data:
                return ImmuDBAdapterResponse(data=count_data['count'])
            else:
                return ImmuDBAdapterResponse(
                    status=False,
                    error="Error: The response obtained from the vault is invalid.",
                    code=500
                )
        
        except httpx.HTTPStatusError as http_err:
            status_code = http_err.response.status_code
    
            if status_code == 400:
                error_message = "Vault: Request validation exception"
            elif status_code == 402:
                error_message = "Vault: Payment required"
            elif status_code == 403:
                error_message = "Vault: Forbidden"
            elif status_code == 404:
                error_message = "Vault: Not found"
            elif status_code == 500:
                error_message = "Vault: Internal server error"
            else:
                error_message = "Vault unknown error."
            
            return ImmuDBAdapterResponse(
                status=False,
                error=error_message,
                code=status_code
            )
        
        except httpx.RequestError:
            return ImmuDBAdapterResponse(
                status=False,
                error="Vault is unreachable.",
                code=500
            )
        except Exception as e:
            return ImmuDBAdapterResponse(
                status=False,
                error=f"Unexpected error with the vault: {str(e)}",
                code=500
            )

    async def get_accounts(self, page: int, count: int) -> ImmuDBAdapterResponse:
        """
        Retrieve a paginated list of accounts from the collection.

        Args:
            page (int): The page number to retrieve.
            count (int): The number of accounts to retrieve per page.

        Returns:
            ImmuDBAdapterResponse: A response object containing the list of accounts
            or an error message in case of failure.
        """
        try:
            accounts_data = await self.client.getData(self.collection_name, page, count)
            
            accounts = []
            for revision in accounts_data.get("revisions", []):
                document = revision.get("document", {})
                account = Account(
                    account_number=document.get("account_number"),
                    account_name=document.get("account_name"),
                    iban=document.get("iban"),
                    address=document.get("address"),
                    amount=document.get("amount"),
                    type=document.get("type")
                )
                accounts.append(account)

            return ImmuDBAdapterResponse(data=accounts)
        
        except httpx.HTTPStatusError as http_err:
            status_code = http_err.response.status_code
    
            if status_code == 400:
                error_message = "Vault: Request validation exception"
            elif status_code == 402:
                error_message = "Vault: Payment required"
            elif status_code == 403:
                error_message = "Vault: Forbidden"
            elif status_code == 500:
                error_message = "Vault: Internal server error"
            else:
                error_message = "Vault unknown error."
            
            return ImmuDBAdapterResponse(
                status=False,
                error=error_message,
                code=status_code
            )
        
        except httpx.RequestError:
            return ImmuDBAdapterResponse(
                status=False,
                error="Vault is unreachable.",
                code=500
            )
        except Exception as e:
            return ImmuDBAdapterResponse(
                status=False,
                error=f"Unexpected error with the vault: {str(e)}",
                code=500
            )

    async def set_accounts(self, account: Account) -> ImmuDBAdapterResponse:
        """
        Set a new account in the collection.

        Args:
            account (Account): The account data to be set or updated.

        Returns:
            ImmuDBAdapterResponse: A response object containing the transaction ID
            or an error message in case of failure.
        """
        try:
            result = await self.client.setData(self.collection_name, account.dict())
            if 'transactionId' in result:
                return ImmuDBAdapterResponse(data=result['transactionId'])
            else:
                return ImmuDBAdapterResponse(
                    status=False,
                    error="Error: The response obtained from the vault is invalid.",
                    code=500
                )
        
        except httpx.HTTPStatusError as http_err:
            status_code = http_err.response.status_code
    
            if status_code == 400:
                error_message = "Vault: Request validation exception"
            elif status_code == 402:
                error_message = "Vault: Payment required"
            elif status_code == 403:
                error_message = "Vault: Forbidden"
            elif status_code == 409:
                error_message = "Vault: Conflict"
            elif status_code == 413:
                error_message = "Vault: Document too big"
            elif status_code == 500:
                error_message = "Vault: Internal server error"
            else:
                error_message = "Vault unknown error."
            
            return ImmuDBAdapterResponse(
                status=False,
                error=error_message,
                code=status_code
            )
        
        except httpx.RequestError:
            return ImmuDBAdapterResponse(
                status=False,
                error="Vault is unreachable.",
                code=500
            )
        
        except Exception as e:
            return ImmuDBAdapterResponse(
                status=False,
                error=f"Unexpected error with the vault: {str(e)}",
                code=500
            )