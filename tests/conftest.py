"""Implementation of pytest fixtures."""
import pytest

from json_app import app


@pytest.fixture(scope="session")
def client() -> None:
    """Pytest fixture for initializing the app and its corresponding test client."""
    # App configuration
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
