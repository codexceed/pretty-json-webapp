from json import JSONDecodeError, dumps, loads


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
        json_obj = loads(text)
        pretty_text = dumps(json_obj, indent=2, sort_keys=True)
    except (JSONDecodeError, TypeError) as e:
        raise InvalidInput(e)

    return pretty_text
