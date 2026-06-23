from unittest.mock import MagicMock

from src.category_iterator import CategoryIterator


class TestCategoryIterator:
    """Тесты для CategoryIterator."""

    def test_iterator_initialization(self):
        """Проверка инициализации итератора."""
        category = MagicMock()
        category.products = ["product1", "product2", "product3"]

        iterator = CategoryIterator(category)

        assert iterator.category == category
        assert iterator.index == 0

    def test_iter_returns_self(self):
        """Проверка, что метод __iter__ возвращает сам итератор."""
        category = MagicMock()
        category.products = []

        iterator = CategoryIterator(category)

        assert iter(iterator) is iterator

    def test_next_returns_products_in_order(self):
        """Проверка последовательного возврата товаров."""
        category = MagicMock()
        category.products = ["product1", "product2", "product3"]

        iterator = CategoryIterator(category)

        assert next(iterator) == "product1"
        assert next(iterator) == "product2"
        assert next(iterator) == "product3"

    def test_next_raises_stop_iteration_at_end(self):
        """Проверка, что StopIteration выбрасывается после окончания товаров."""
        category = MagicMock()
        category.products = ["product1", "product2"]

        iterator = CategoryIterator(category)

        next(iterator)
        next(iterator)
