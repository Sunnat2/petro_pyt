import json

class Contact:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class PhoneBook:
    def __init__(self, filename='contacts.json'):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact.dict)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                print(contact)
                return contact
        print("Contact not found")
        return None

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()

    def update_contact(self, name, new_contact):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.contacts.append(new_contact.dict)
            self.save_contacts()

def main():
    phonebook = PhoneBook()
    
    while True:
        print("1. View contacts")
        print("2. Add contact")
        print("3. Find contact")
        print("4. Delete contact")
        print("5. Update contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            phonebook.view_contacts()
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            contact = Contact(name, phone, email)
            phonebook.add_contact(contact)
        elif choice == '3':
            name = input("Enter name to find: ")
            phonebook.find_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            phonebook.delete_contact(name)
        elif choice == '5':
            name = input("Enter name to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email (optional): ")
            new_contact = Contact(new_name, new_phone, new_email)
            phonebook.update_contact(name, new_contact)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "main":
    main()