from src.product import Product


class Category:
    """Класс категорий продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description,products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products) if products else 0


    def add_product(self, product):
        """ Метод для добавления продуктов в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для получения списка продуктов"""
        return self.__products

    @property
    def printing_products_list(self):
        """ Метод для вывода списка продуктов в категории"""
        str_products = ""
        for product in self.__products:
            str_products += f"{product.name},  {product.price} руб. Остаток: {product.quantity} шт\n"
        return str_products




