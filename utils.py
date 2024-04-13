from abc import ABC, abstractmethod

class CreationLoggerMixin:
    def log_creation(self):
        print(f"Создан объект класса {self.__class__.__name__} с атрибутами:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class AbstractProduct(ABC):
    total_unique_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        AbstractProduct.total_unique_products += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self._price = new_price

    @abstractmethod
    def display_info(self):
        pass

class Product(AbstractProduct, CreationLoggerMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.log_creation()

    def display_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class Smartphone(AbstractProduct, CreationLoggerMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color
        self.log_creation()

    def display_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. Модель: {self.model}"

class Grass(AbstractProduct, CreationLoggerMixin):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        self.log_creation()

    def display_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. Страна происхождения: {self.country_of_origin}"

if __name__ == '__main__':
    smartphone = Smartphone("iPhone", "Apple iPhone", 1000, 1, "High", "X", "64GB", "Silver")
    product = Product("Book", "Interesting book", 20, 5)

    print(smartphone.display_info())
    print(product.display_info())



