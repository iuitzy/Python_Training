class Product:
    def __init__(self, name, category, price):
        self._product = (name, category, price)  # Store product as an immutable tuple
    
    def get_details(self):
        return self._product  # Return the tuple containing product details
