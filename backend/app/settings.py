import os
from app.utils import str_to_bool

class Settings:
    """
    Singleton class to manage application settings.

    This class loads configuration values from environment variables and 
    ensures that only one instance of the settings is created during the 
    application's lifetime. Accessing the settings via `Settings()` will 
    always return the same instance.
    """

    _instance = None

    def __new__(cls):
        """
        Create or return the existing instance of the Settings class.

        If no instance exists, this method will create a new one. Otherwise, 
        it will return the already initialized instance, ensuring a single 
        instance of the class.
        
        Returns:
            Settings: The singleton instance of the Settings class.
        """
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """
        Initialize the settings by loading environment variables.

        This method is called only once to set up the instance variables based 
        on environment variables. It handles the default values if the 
        environment variables are not set.
        """
        stringSandboxValue = os.getenv("IMMUDB_VAULT_SANDBOX", "1")
        self.IMMUDB_VAULT_SANDBOX = str_to_bool(stringSandboxValue)
        self.IMMUDB_VAULT_LEDGER_NAME = os.getenv("IMMUDB_VAULT_LEDGER_NAME", "default")
        self.IMMUDB_VAULT_COLLECTION_NAME = os.getenv("IMMUDB_VAULT_COLLECTION_NAME", "accounts")
        self.IMMUDB_VAULT_BASEURL = os.getenv("IMMUD_DB_URL", "https://vault.immudb.io/ics/api/v1")
        self.IMMUDB_VAULT_API_KEY = os.getenv("IMMUD_DB_API_KEY", "XXXXXXXXXXXXXXXXX")
        self.FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")