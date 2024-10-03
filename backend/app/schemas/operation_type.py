from enum import Enum

class OperationType(str, Enum):
    """
    Enumeration for the type of account operation.

    Attributes:
        SENDING (str): Represents an account used for sending transactions.
        RECEIVING (str): Represents an account used for receiving transactions.
    """
    
    SENDING = 'sending'
    RECEIVING = 'receiving'