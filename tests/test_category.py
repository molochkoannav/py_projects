from src.category import Category


def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3
    assert category1.products[0].name == "iPhone 13"
    assert category1.products[1].name == "Samsung Galaxy S22"


def test_category_count(category1):

    assert Category.category_count >= 1


def test_product_count(category1):
    assert Category.product_count >= 2
