import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        file = open('contacts.json', 'r')
        self.contacts = json.load(file)['contacts']

    def count(self):
        return len(self.contacts)
    
    def save(self):
        with open('contacts.json', 'w') as file:
            json.dump({'contacts': self.contacts}, file)

    def print(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone number: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print()

    def add(self, name, phone_number, email):
        self.contacts.append({'name': name, 'phone_number': phone_number, 'email': email})
    
    def remove(self, name):
        self.contacts[:] = [c for c in self.contacts if c['name'] != name]

    def update(self, old_name, new_name, new_phone_number, new_email):
        for contact in self.contacts:
            if contact['name'] == old_name:
                contact.update({'name': new_name, 'phone_number': new_phone_number, 'email': new_email})

contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded ${contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved ${contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contact_list.remove(name)
    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ')
        new_name = input('New Name: ')
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ')
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')