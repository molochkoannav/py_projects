from src.product import Product


def test_product_init(product1):
    """Тест на инициализацию"""
    assert product1.name == "iPhone 13"
    assert product1.description == "Смартфон Apple iPhone 13"
    assert product1.price == 79990.0
    assert product1.quantity == 10


def test_new_product():
    """Тест на ввод нового продукта"""
    product = Product("iPhone 15", "Смартфон Apple iPhone 15", 150000.0, 10)
    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple iPhone 15"
    assert product.price == 150000.0
    assert product.quantity == 10


def test_new_product_is_double():
    """Тест если продукт уже есть в списке"""
    existing_product = Product("iPhone 15", "Смартфон Apple iPhone 15", 120000.0, 10)
    existing_products = [existing_product]

    product_data = {"name": "iPhone 15", "description": "Смартфон Apple iPhone 15", "price": 150000.0, "quantity": 10}
    new_product = Product.new_product(product_data, existing_products)

    assert new_product is existing_product
    assert new_product.quantity == 20
    assert new_product.price == 150000.0
    assert new_product.name == "iPhone 15"
    assert new_product.description == "Смартфон Apple iPhone 15"


def test_price_property():
    """Тест с выводом цены"""
    product = Product("iPhone 15", "Смартфон Apple iPhone 15", 150000.0, 10)
    assert product.price == 150000.0


def test_new_price_setter():
    """Тест: несколько операций с ценой"""
    product = Product("Телефон", "Описание", 1000.0, 5)
    product.price = 1500.0
    assert product.price == 1500.0

    product.price = -100.0
    assert product.price == 1500.0


def test_set_price_decrease_with_monkeypatch(monkeypatch):
    """Тест с использованием monkeypatch для имитации ввода"""
    product = Product("Телефон", "Описание", 1000.0, 5)

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 800.0
    assert product.price == 800.0
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 600.0
    assert product.price == 800.0  # Цена не изменилась


def test_str():
    """Тест на вывод информации о товаре"""
    product = Product("iPhone 15", "Смартфон Apple iPhone 15", 150000.0, 10)
    assert str(product) == "iPhone 15, 150000.0 руб. Остаток: 10 шт."


def test_mul():
    """Тест на расчет общей стоимости продукта на складе"""
    product = Product("iPhone 15", "Смартфон Apple iPhone 15", 150000.0, 10)
    other = 10
    assert product * 2 * other == 30000000.0
    other = None
    assert product * 0.5 == 750000.0
    other = "string"
    try:
        product * other
        assert False, "Ожидалось исключение TypeError"
    except TypeError as e:
        assert str(e) == "Нельзя умножить Product с str"


def test_add():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 2580000.0
