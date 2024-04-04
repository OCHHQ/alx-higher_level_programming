def say_my_name(first_name, last_name=""):
    """
    Print 'My name is <first name> <last name>'.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")

