class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.category.products):
            raise StopIteration
        product = self.category.products[self.index]
        self.index += 1
        return product
