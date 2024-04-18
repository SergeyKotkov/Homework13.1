class AbstractProduct:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class CreationLoggerMixin:
    def log_creation(self):
        print(f"Создан товар: {self.name}")

class Product(AbstractProduct, CreationLoggerMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.log_creation()

    def __str__(self):
        return f"{self.name} - Цена: {self.price}, Количество: {self.quantity}"

class Category:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product!")
        if product.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством!")
        else:
            self.products.append(product)

    def calculate_average_price(self):
        total_price = sum(product.price for product in self.products)
        total_quantity = sum(product.quantity for product in self.products)

        if total_quantity == 0:
            print("Ошибка: В категории нет товаров.")
            return 0

        return total_price / total_quantity

# Пример использования
product1 = Product("Шоколад", "Вкусный шоколад", 100, 10)
smartphone1 = Product("Смартфон", "Последняя модель", 500, 5)
grass1 = Product("Трава", "Зеленая трава", 0, 0)

category1 = Category()
category1.add_product(product1)
category1.add_product(smartphone1)
category1.add_product(grass1)

for product in category1.products:
    print(product)

average_price = category1.calculate_average_price()
print(f"Средний ценник всех товаров в категории: {average_price}")
