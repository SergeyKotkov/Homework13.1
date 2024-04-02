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

    @classmethod
    def create_product(cls, data):
        return Product(**data)


class Product:
    total_unique_products = 0
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_unique_products += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self._price = new_price

    @classmethod
    def create_product(cls, data):
        return cls(**data)


if __name__ == '__main__':

    prod_1 = Category('Яблоки', 'сладкие')
    prod_2 = Category('Бананы', 'спелые')
    prod_3 = Category('Яблоки', 'кислые')
    prod_4 = Category('Конфеты', 'вкусные')
    prod_5 = Category('Картофель', 'крупная')

    Prod_1 = Product('Яблоки', 'сладкие', 50, 100)
    Prod_2 = Product('Бананы', 'спелые', 100, 200)
    Prod_3 = Product('Конфеты', 'сладкие', 75, 1000)
    Prod_4 = Product('Картофель', 'крупный', 65, 2000)

print(f'{Category.total_uniq_products}')