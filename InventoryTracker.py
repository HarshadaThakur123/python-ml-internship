inventory = []  # List to store items as dictionaries

# Function to add a new item
def add_item():
    name = input("Enter item name: ").strip()
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        item = {'name': name, 'price': price, 'quantity': quantity}
        inventory.append(item)
        print(f"Item '{name}' added successfully.")
    except:
        print("Invalid input. Please enter numeric values for price and quantity.")

# Function to view all items
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Inventory List ---")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. Name: {item['name']}, Price: ₹{item['price']}, Quantity: {item['quantity']}")
    print("----------------------")

# Function to update quantity
def update_quantity():
    name = input("Enter the name of the item to update: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            try:
                new_qty = int(input("Enter new quantity: "))
                item['quantity'] = new_qty
                print(f"Quantity for '{name}' updated to {new_qty}.")
                return
            except:
                print("Invalid quantity.")
                return
    print(f"Item '{name}' not found.")

# Function to remove an item
def remove_item():
    name = input("Enter the name of the item to remove: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            return
    print(f"Item '{name}' not found.")

# Main loop
def inventory_menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting Inventory Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

# Run the program
inventory_menu()
