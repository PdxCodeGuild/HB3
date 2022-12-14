# Lab 09 -> write a python class for managing a contact list.

import json

class ContactList:
    def __init__(self):
        self.contacts = []
    
    def load(self):
        file = open(r'contacts.json')
        file_data = file.read()
        file_data = json.loads(file_data)
        self.contacts = file_data['contacts']
        return self.contacts

    def count(self):
        return len(self.contacts)

    def save(self):
        with open('contacts.json', 'w') as f:
            new_dict = {'contacts': self.contacts}
            new_dict = json.dumps(new_dict)
            f.write(new_dict)

    def print(self):
        for contact in self.contacts:
            print(contact)

    def add(self, name, phone_number, email):
        new_dict = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(new_dict)

    def remove(self, name):
        for x in self.contacts:
            if x['name'].lower() == name.lower():
                self.contacts.remove(x)

    def update(self, old_name, new_name, new_phone_number, new_email):
        for x in self.contacts:
            if x['name'].lower() == old_name.lower():
                self.contacts.remove(x)
                new_dict = {'name': new_name,'phone_number': new_phone_number, 'email': new_email}
                self.contacts.append(new_dict)

contact_list = ContactList()  # create an instance of our class
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count()} contacts.')
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