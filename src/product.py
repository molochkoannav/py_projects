class Product:
    """Класс для создания и работы с товарами"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __mul__(self, other=None):
        """Возвращает общую стоимость продукта на складе"""
        if other is None:
            return self.__price * self.quantity
        elif isinstance(other, (int, float)):
            return self.__price * self.quantity * other
        else:
            raise TypeError(f"Нельзя умножить Product с {type(other).__name__}")

    def __add__(self, other):
        """Сложение продуктов по общей стоимости"""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """Метод добавления продуктов с проверкой на дублирование"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        if existing_products is not None:
            for product in existing_products:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Вывод цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метов для изменения цены с подтверждением у пользователя"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer_user = input(f"Понизить цену с {self.__price} до {new_price}? y/n ")
            if answer_user.lower() == "y":
                self.__price = new_price
                print(f"Цена успешно понижена до {new_price}")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price

