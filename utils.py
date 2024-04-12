class Category:
    total_categories = 0
    total_products = set()
    total_uniq_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        for product in self.__products:
            Category.total_products.add(product)
        Category.total_uniq_products = len(Category.total_products)
        Category.total_categories += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("В категорию можно добавлять только экземпляры класса Product или его подклассов")

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            products_info.append(info)
        return products_info

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(Category.total_products)} шт."


class Product:
    total_unique_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_unique_products += 1

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Невозможно добавить товары разных типов")

        total_quantity = self.quantity + other.quantity
        total_price = self.price + other.price
        return Product(f"Комбинированный {self.name} и {other.name}", "Комбинированный продукт", total_price, total_quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self._price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value

    @classmethod
    def create_product(cls, data):
        return cls(**data)

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color

class Grass(Product):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


if __name__ == 'main':
    prod_1 = Category('Яблоки', 'сладкие')
    prod_2 = Category('Бананы', 'спелые')
    prod_3 = Category('Яблоки', 'кислые')
    prod_4 = Category('Конфеты', 'вкусные')
    prod_5 = Category('Картофель', 'крупная')

    Prod_1 = Product('Яблоки', 'сладкие', 50, 100)
    Prod_2 = Product('Бананы', 'спелые', 100, 200)
    Prod_3 = Product('Конфеты', 'сладкие', 75, 1000)
    Prod_4 = Product('Картофель', 'крупный', 65, 2000)

    smartphone = Smartphone("iPhone", "Apple iPhone", 1000, 1, "High", "X", "64GB", "Silver")
    product = Product("Book", "Interesting book", 20, 5)



