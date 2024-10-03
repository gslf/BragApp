def str_to_bool(stringValue, default=True):
    """
    Converts a string representation of a boolean value to a boolean.

    The method checks if the input string is one of the commonly accepted 
    truthy values ('1', 'true', 'yes', 'on'). If the input string matches 
    any of these values (case-insensitive), the method returns `True`. 
    Otherwise, it returns `False`.

    Args:
        stringValue (str): The string to convert to a boolean.
        default (bool, optional): Default value to return if the string 
            doesn't match any truthy value. Defaults to `True`.

    Returns:
        bool: The boolean value corresponding to the input string.
    """
    
    return stringValue.lower() in ('1', 'true', 'yes', 'on')