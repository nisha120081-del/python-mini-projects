print("welcome to the contact book system")
contacts = {}

def add_contact():
    name = input("Enter contact name:")
    phone = input("Enter contact phone number:")
    contacts[name] = phone
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("Contacts:")
        for i in contacts:
            print(f"{i}: {contacts[i]}")
    else:
        print("No contacts found.")

def delete_contact():
    name = input("Enter contact name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def search_contact():
    name = input("Enter contact name to search:")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Exiting the contact book system.")
        break
    else:
        print("Invalid choice. Please try again.")