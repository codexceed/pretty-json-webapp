"""Implementation of tests for json parsing module."""
import pytest

from json_app.parse_json.parser import InvalidInput, prettify
from tests.cases import *


@pytest.mark.parametrize(
    "input_string,validation_string",
    zip(successful_parsing_cases, successful_parsing_validation),
)
def test_json_prettify_success(input_string: str, validation_string: str) -> None:
    """Validate pretty json success cases."""
    assert prettify(input_string) == validation_string


@pytest.mark.parametrize("input_string", error_cases)
def test_json_prettify_failure(input_string: str) -> None:
    """Validate pretty json failure cases. """
    with pytest.raises(InvalidInput):
        prettify(input_string)
