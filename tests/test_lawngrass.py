import pytest

def test_lawngrass_init(lowngrass1):
    """Тест на инициализацию"""
    assert lowngrass1.name == "Газонная трава"
    assert lowngrass1.description == "Элитная трава для газона"
    assert lowngrass1.price == 500.0
    assert lowngrass1.quantity == 20
    assert lowngrass1.country == "Россия"
    assert lowngrass1.germination_period == "7 дней"
    assert lowngrass1.color == "Зеленый"


def test_lawngrass_add(lowngrass1, lowngrass2):
    """Тест на сложение правильных категорий"""
    assert lowngrass1 + lowngrass2 == 16750


def test_smartphone_add_error(lowngrass1):
    """Тест на сложение категорий с ошибкой"""
    with pytest.raises(TypeError):
        result = lowngrass1 + 1
