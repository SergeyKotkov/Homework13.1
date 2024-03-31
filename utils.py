class Category:
    name: str
    description: str
    product: list
    total_categories = 0
    uniq_products = set()
    total_uniq_products = str

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        for product in products:
            if product not in Category.uniq_products:
                Category.uniq_products.add(product)
        Category.total_uniq_products = len(Category.uniq_products)


class Product():
    name: str
    description: str
    product: list
    price: float
    stock: int

    def __init__(self, name, description, product, price, stock):
        self.price = price
        self.stock = stock
        self.name = name
        self.description = description
        self.product = product

if __name__ == '__main__':

    prod_1 = Category('Яблоки', 'сладкие', ("фрукт", "красные"))
    prod_2 = Category('Бананы', 'спелые', ('фрукт', 'желтые'))
    prod_3 = Category('Яблоки', 'кислые', ('фрукт', 'зеленые'))
    prod_4 = Category('Конфеты', 'вкусные', ('сладости', 'шоколадные'))
    prod_5 = Category('Картофель', 'крупная', ('овощи', 'мытый'))

    Prod_1 = Product('Яблоки', 'сладкие', ("фрукт", "красные"),50, 100)
    Prod_2 = Product('Бананы', 'спелые', ("фрукт", "желтые"),100, 200)
    Prod_3 = Product('Конфеты', 'сладкие', ("сладости", "шоколадные"),75, 1000)
    Prod_4 = Product('Картофель', 'крупный', ("овощи", "мытый"),65, 2000)

    print(f'{prod_1.total_categories}')
    print(f'{prod_2.products}')
    print(f'{prod_3.name}')
    print(f'{prod_4.description}')
    print(f'{Prod_1.price}', f'{Prod_1.stock}')
    print(f'{Prod_2.description}')
    print(f'{Prod_3.product}')
    print(f'{Category.total_uniq_products}')
