from item_manager import ItemManager

def main():
    manager = ItemManager()

    # Adding items (ID is randomly generated)
    manager.create_item("Laptop", "Asus Rog Strix G16", 1200.99)
    manager.create_item("Phone", "Iphone 16E", 799.49)
    
    manager.list_items()  # Show all items

    # Prompt user to add a new item
    name = input("Enter item name: ")
    description = input("Enter item description: ")
    price = float(input("Enter item price: "))

    manager.create_item(name, description, price)
    
    manager.list_items()  # Show updated list

if __name__ == "__main__":
    main()
