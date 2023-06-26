import pytest
from homework_26.services.store import StoreService


@pytest.fixture
def store_service():
    yield StoreService()
