class Category:
    name: str
    description: str
    product: list
    total_categories = 0
    total_uniq_products = set()

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        for product in products:
            Category.total_uniq_products.add(product.name)





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

