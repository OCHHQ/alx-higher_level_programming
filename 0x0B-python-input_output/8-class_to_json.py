#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: Dictionary description of the object.
    """
    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

    return result

