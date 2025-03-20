import random
import string

class Item:
    """Represents an item with a random 5-character ID, name, description, and price."""
    
    def __init__(self, name: str, description: str, price: float):
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Item description must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Item price must be a non-negative number.")

        self.item_id = self.generate_id()
        self.name = name.strip()
        self.description = description.strip()
        self.price = round(price, 2)

    @staticmethod
    def generate_id():
        """Generates a unique random 5-character alphanumeric ID."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Price: ${self.price:.2f}"