class Product:
    def __init__(self, name, id, price, rating, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.rating = rating
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def remove_stock(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity to remove.")
        self.quantity -= quantity

    def update_rating(self, rating):
        self.rating = rating

    def update_price(self, price):
        self.price = price

    def __str__(self):
        return f"{self.name}, ID: {self.id}, Price: {self.price}, Rating: {self.rating}, Quantity: {self.quantity}"


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break
        else:
            raise ValueError("No product found.")

    def get_item(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        else:
            raise ValueError("No product found.")

    def __str__(self):
        return f"{self.name}: {[product.name for product in self.products]}"


category = Category("Clothes")
product1 = Product("t-shirt", 123, 999, 4.6, 110)
product2 = Product("jeans", 321, 899, 4.2, 60)

category.add_item(product1)
category.add_item(product2)

print(category)

category.remove_item(321)
print(category)

product = category.get_item(123)
print(product)


class Basket:
    def __init__(self):
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break
        else:
            raise ValueError("No product found.")

    def get_item(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        else:
            raise ValueError("No product found.")

    def make_purchase(self, product_ids):
        purchased_products = []
        for product_id in product_ids:
            product = self.get_item(product_id)
            self.remove_item(product_id)
            purchased_products.append(product.name)
        return purchased_products

    def __str__(self):
        return f"Basket: {[product.name for product in self.products]}"


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.basket = Basket()

    def __str__(self):
        return f"User: {self.login}"

    def add_to_basket(self, product):
        self.basket.add_item(product)

    def remove_from_basket(self, product_id):
        self.basket.remove_item(product_id)

    def make_purchase(self, product_ids):
        return self.basket.make_purchase(product_ids)

    def get_basket(self):
        return self.basket


user1 = User("login", "password")
user2 = User("l0gin", "passw0rd")

