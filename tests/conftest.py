import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product(
        name="iPhone 13",
        description="Смартфон Apple iPhone 13",
        price=79990,
        quantity=10,
    )


@pytest.fixture
def product2():
    return Product(
        name="Samsung Galaxy S22",
        description="Смартфон Samsung Galaxy S22",
        price=69990,
        quantity=5,
    )


@pytest.fixture
def product3():
    return Product(
        name="Xiaomi Redmi Note 10",
        description="Смартфон Xiaomi Redmi Note 10",
        price=39990,
        quantity=15,
    )


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product(
                name="iPhone 13",
                description="Смартфон Apple iPhone 13",
                price=79990,
                quantity=10,
            ),
            Product(
                name="Samsung Galaxy S22",
                description="Смартфон Samsung Galaxy S22",
                price=69990,
                quantity=5,
            ),
            Product(
                name="Xiaomi Redmi Note 10",
                description="Смартфон Xiaomi Redmi Note 10",
                price=39990,
                quantity=15,
            ),
        ],
    )


def category2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product(
                name='55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            )
        ],
    )
