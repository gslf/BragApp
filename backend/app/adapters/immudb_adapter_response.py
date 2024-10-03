from typing import Any

class ImmuDBAdapterResponse:
    """
    A class to represent a response from the ImmuDB adapter.

    This class encapsulates the response status, any error message, 
    an HTTP-like status code, and the associated data from a database query.

    Attributes:
        status (bool): A boolean indicating whether the request was successful. Defaults to True.
        error (str): A string containing an error message, if applicable. Defaults to an empty string.
        code (int): An integer representing the response code (e.g., HTTP status code). Defaults to 200.
        data (Any): The data returned from the query or operation. Defaults to None.

    """

    def __init__(self, status: bool = True, error: str = "", code: int = 200, data: Any = None):
        """
        Initializes an instance of ImmuDBAdapterResponse with the given parameters.

        Args:
            status (bool, optional): A boolean indicating whether the request was successful. Defaults to True.
            error (str, optional): A string containing an error message, if any. Defaults to an empty string.
            code (int, optional): An integer representing the response code (e.g., HTTP status code). Defaults to 200.
            data (Any, optional): The data returned from the query or operation. Defaults to None.
        """

        self.status = status
        self.error = error
        self.code = code
        self.data = data