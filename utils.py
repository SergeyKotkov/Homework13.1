class AbstractProduct:
    def __init__(self):
        pass

    def init(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class CreationLoggerMixin:
    def log_creation(self):
        print(f"Создан товар: {self.name}")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Category:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_average_price(self):
        total_price = sum(product.price for product in self.products)
        total_quantity = sum(product.quantity for product in self.products)

        try:
            average_price = total_price / total_quantity
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль. В категории нет товаров.")
            return 0

        return average_price

# Пример использования
product1 = Product("Шоколад", 100, 10)
smartphone1 = Product("Смартфон", 500, 5)
grass1 = Product("Трава", 0, 0)

category1 = Category()
category1.add_product(product1)
category1.add_product(smartphone1)
category1.add_product(grass1)

average_price = category1.calculate_average_price()
print(f"Средний ценник всех товаров в категории: {average_price}")
