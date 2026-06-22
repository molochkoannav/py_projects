class Category:
    """Класс категорий продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_quantity = 0
        for product in self.products:
            if hasattr(product, 'quantity'):
                total_quantity += product.quantity
            else:
                print(f"Предупреждение: {product} не является объектом продукта")
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Метод для добавления продуктов в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_obj(self):
        """Геттер для получения списка продуктов"""
        return self.__products

    @property
    def products(self):
        """Геттер для получения списка продуктов """
        str_products = ""
        for product in self.__products:
            str_products += f"Ъ{str(product)} шт\n"
        return str_products

