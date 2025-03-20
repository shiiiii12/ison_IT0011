from item_manager import ItemManager

def main():
    manager = ItemManager()

    manager.create_item("Laptop", "Asus Rog Strix G16", 1200.99)
    manager.create_item("Phone", "Iphone 16E", 799.49)
    
    manager.list_items()

    name = input("Enter item name: ")
    description = input("Enter item description: ")
    price = float(input("Enter item price: "))

    manager.create_item(name, description, price)
    
    manager.list_items()

if __name__ == "__main__":
    main()
