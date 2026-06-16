import json
import os.path
import os

from src.product import Product
from src.category import Category


def read_json_file(file_path: str) -> dict:
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_obj_from_json(data: dict) -> list:
    categories_data = []

    for category_data in data:
        products = []
        products_data = category_data.get("products", [])

        for product_data in products_data:
            products.append(Product(**product_data))

        category_copy = category_data.copy()
        category_copy["products"] = products

        categories_data.append(Category(**category_copy))

    return categories_data


if __name__ == "__main__":
    data = read_json_file("../data/products.json")
    objects_data = create_obj_from_json(data)
    print(objects_data)