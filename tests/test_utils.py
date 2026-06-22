import json
from unittest.mock import mock_open
from unittest.mock import patch


def test_read_json_file():
    """Тест чтения JSON файла"""
    test_data = {"name": "Test", "products": []}
    mock_json = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=mock_json)):
        with patch("os.path.abspath", return_value="/fake/path/file.json"):
            from src.utils import read_json_file

            result = read_json_file("file.json")

    assert result == test_data


def test_create_obj_from_json():
    """Тест создания объектов из JSON"""
    from src.category import Category
    from src.product import Product

    test_data = [
        {
            "name": "Electronics",
            "description": "Devices",
            "products": [{"name": "Laptop", "description": "Powerful", "price": 1000.0, "quantity": 5}],
        }
    ]

    from src.utils import create_obj_from_json

    result = create_obj_from_json(test_data)

    assert len(result) == 1
    assert isinstance(result[0], Category)
    assert len(result[0].products_obj) == 1
    assert isinstance(result[0].products_obj[0], Product)


def test_create_obj_from_json_empty():
    """Тест с пустым списком продуктов"""
    from src.category import Category

    test_data = [{"name": "Empty", "description": "No products", "products": []}]

    from src.utils import create_obj_from_json

    result = create_obj_from_json(test_data)

    assert len(result) == 1
    assert isinstance(result[0], Category)
    assert len(result[0].products_obj) == 0
