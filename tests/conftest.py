import pytest
from tests.utils import APIClient 

# tests/conftest.py
@pytest.fixture(scope="session")
def api_client():
    return APIClient()