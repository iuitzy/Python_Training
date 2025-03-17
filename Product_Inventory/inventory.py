""" Assignment 3: Product Inventory
Create a program that maintains an inventory of products using tuples. Each product should have a name, category, and price. Ensure products cannot be modified after creation but allow viewing them.
Expected Output:
- Display all products with their details
- Attempting to modify a product should raise an error
"""




from Product import Product

class Inventory:
    def __init__(self):
        self.products = []  # List to store product tuples

    def add_product(self, name, category, price):
        product = Product(name, category, price)
        self.products.append(product)
        print(f"Product '{name}' added successfully.")
    
    def display_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        print("\nProduct Inventory:")
        for product in self.products:
            name, category, price = product.get_details()
            print(f"Name: {name}, Category: {category}, Price: {price}")