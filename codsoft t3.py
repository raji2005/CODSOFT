class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append(Contact(name, phone, email, address))
    print("Contact added successfully!")

def view_contact_list():
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone}")

def search_contact(query):
    for contact in contacts:
        if query in contact.name or query in contact.phone:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact.name == name:
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            contact.address = input("Enter new address: ")
            print("Contact updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")

while True:
    print("\nContact Management System\n")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        search_contact(query)
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice")
