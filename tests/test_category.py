from src.category import Category
from src.product import Product


def test_category_init(category1):
    """Тест на инициализацию"""
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert category1.products_obj[0].name == "iPhone 13"
    assert category1.products_obj[1].name == "Samsung Galaxy S22"


def test_product_count(category1):
    """Тест проверки счетчика"""
    assert Category.product_count >= 2


def test_category_add_product(category1, product1):
    """Тест на правильность добавления через add_product"""
    category1.add_product(product1)
    assert category1.products_obj[3].name == "iPhone 13"
    assert len(category1.products_obj) == 4


def test_products_obj(category1):
    """Тест на правильность работы property products"""
    assert category1.products_obj[0].name == "iPhone 13"
    assert category1.products_obj[1].name == "Samsung Galaxy S22"
    assert len(category1.products_obj) == 3


def test_products():
    """Тест на правильность вывода строки с продуктами"""
    category = Category("Смартфоны", "Смартфоны, как средство коммуникации", [])
    assert category.products == ""


def test_str():
    """Тест вывода строки"""
    product1 = Product("iPhone 15", "Смартфон Apple iPhone 15", 150000.0, 10)
    product2 = Product("Samsung Galaxy", "Смартфон Samsung", 100000.0, 5)
    product3 = Product("Xiaomi", "Смартфон Xiaomi", 50000.0, 3)
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product1, product2, product3])

    assert str(category1) == "Смартфоны, Смартфоны, как средство не только коммуникации, количество продуктов: 18 шт."
