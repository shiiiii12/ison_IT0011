from item import Item

class ItemManager:
    """Manages a collection of items with CRUD operations."""
    
    def __init__(self):
        self.items = {}

    def create_item(self, name, description, price):
        """Adds a new item with a random ID."""
        try:
            item = Item(name, description, price)
            self.items[item.item_id] = item
            print(f"Item added successfully! ID: {item.item_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id):
        """Retrieves an item by ID."""
        item = self.items.get(item_id)
        print(item if item else "Item not found.")

    def update_item(self, item_id, name=None, description=None, price=None):
        """Updates an item's attributes."""
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return

        try:
            if name:
                item.name = name.strip()
            if description:
                item.description = description.strip()
            if price is not None:
                if not isinstance(price, (int, float)) or price < 0:
                    raise ValueError("Price must be a non-negative number.")
                item.price = round(price, 2)
            print("Item updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        """Removes an item by ID."""
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully.")
        else:
            print("Item not found.")

    def list_items(self):
        """Displays all items."""
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)