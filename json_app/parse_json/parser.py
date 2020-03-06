import json


class InvalidInput(Exception):
    pass


def prettify(text: str) -> str:
    """
    Rearrange the elements in a valid json string in a prettier fashion.

    Args:
        text: Valid json text to be prettified.

    Returns:
        Pretty text.
    """
    pretty_text = ""
    try:
        json_obj = json.loads(text)
        pretty_text = json.dumps(json_obj, indent=2, sort_keys=True)
    except json.JSONDecodeError as e:
        InvalidInput(e)

    return pretty_text
