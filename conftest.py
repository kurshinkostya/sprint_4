import pytest
from main import BooksCollector

# создаем фикстуру collector
@pytest.fixture
def collector():
    return BooksCollector()