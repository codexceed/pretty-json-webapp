"""Implementation of API endpoint routes."""
from typing import Any

import pytest

from json_app import routes
from json_app.constants import HOME_TITLE
from tests.cases import *

# Constants
BASE_URL = "http://127.0.0.1:5000"


def test_index_redirect(client: Any) -> None:
    """Test redirection to pretty-json page from '/' route."""
    # Perform assertions
    assert client.get(f"{BASE_URL}/").location == f"{BASE_URL}/prettify-json"


def test_get_pretty_json(client: Any, mocker: Any) -> None:
    """Test 'GET' call on '/prettify-json' endpoint."""
    # Create spies
    render_template = mocker.spy(routes, "render_template")

    # Perform the actual request
    client.get(f"{BASE_URL}/prettify-json")

    # Assertions
    render_template.assert_called_once_with("prettyjson.html", title=HOME_TITLE)


@pytest.mark.parametrize(
    "request_data, response_json",
    zip(successful_parsing_cases, successful_parsing_validation),
)
def test_prettify_json_valid(
    client: Any, mocker: Any, request_data: str, response_json: str
) -> None:
    """Test prettify request with valid json strings."""
    # Create spies
    prettify = mocker.spy(routes, "prettify")
    render_template = mocker.spy(routes, "render_template")

    # Perform the actual request
    data = {"json-input": request_data}
    client.post(f"{BASE_URL}/prettify-json", data=data)

    # Assertions
    prettify.assert_called_once_with(text=request_data)
    render_template.assert_called_once_with(
        "prettyjson.html", title=HOME_TITLE, json_output=response_json
    )


@pytest.mark.parametrize("request_data", error_cases)
def test_prettify_json_invalid(client: Any, mocker: Any, request_data: str) -> None:
    """Test prettify request with invalid json strings."""
    # Create spies
    prettify = mocker.spy(routes, "prettify")

    # Perform the actual request
    data = {"json-input": request_data}
    response = client.post(f"{BASE_URL}/prettify-json", data=data)

    # Assertions
    prettify.assert_called_once_with(text=request_data)
    assert response.data == b"Invalid json string."
