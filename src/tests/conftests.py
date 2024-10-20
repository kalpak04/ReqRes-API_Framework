import pytest
from src.utils.api_helper import APIHelper

@pytest.fixture(scope="session")
def api_helper():
    return APIHelper()
