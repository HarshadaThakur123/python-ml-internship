# Contact Book Manager

# Dictionary to store contacts
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contact_book:
        print("Contact already exists.")
    else:
        number = input("Enter contact number: ").strip()
        contact_book[name] = number
        print("Contact added successfully.")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, number in contact_book.items():
            print(f"Name: {name}, Number: {number}")
        print("--------------------")

# Function to search for a contact
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        print(f"Found: Name: {name}, Number: {contact_book[name]}")
    else:
        print("Contact not found.")

# Main function to run the contact book
def contact_book_manager():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Start the program
contact_book_manager()
