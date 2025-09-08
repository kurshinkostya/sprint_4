import pytest
from main import BooksCollector

# фикстура для collector
@pytest.fixture
def collector():
    return BooksCollector()