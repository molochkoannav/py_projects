import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
@pytest.fixture
def smartphone1():
    return Smartphone(
                      name="Iphone 15",
                      description="512GB, ""Gray space",
                      price=210000.0,
                      quantity=8,
                      efficiency=98.2,
                      model="15",
                      memory=512,
                      color="Gray space"
                      )


@pytest.fixture
def smartphone2():
    return Smartphone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=90.3,
        model="Note 11",
        memory=1024,
        color="Синий"
    )

@pytest.fixture
def lowngrass1():
    return LawnGrass(
                name="Газонная трава",
                description="Элитная трава для газона",
                price=500.0,
                quantity=20,
                country="Россия",
                germination_period="7 дней",
                color="Зеленый"
    )

@pytest.fixture
def lowngrass2():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )