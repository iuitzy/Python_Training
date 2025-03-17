from Product import Product
from inventory import Inventory

def main():
    inventory = Inventory()
    inventory.add_product("Laptop", "Electronics", 80000)
    inventory.add_product("Table", "Furniture", 5000)
    inventory.display_products()

if __name__ == "__main__":
    main()
