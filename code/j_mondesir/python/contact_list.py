import os
import json
#list_contact = input('Upload your contact list: ')
class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        with open("contacts.json", 'r') as open_file:
            read_file = open_file.read()
            convert_file = json.loads(read_file)
            self.contacts = convert_file['contacts']
        print('Upload successful! ')
        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        ...
    def count(self):
        return len(self.contacts)
        ...
    def save(self):
        with open("contacts.json", 'w') as open_file:
            my_dictionary = {'contacts': self.contacts}
            open_file.write(json.dumps(my_dictionary))
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        ...

    def print(self):
        for contacts in self.contacts:
            print(contacts)
        # loop over self.contacts
        # print the information for each contact on a separate line
        

    def add(self, name, phone_number, email):
        new_contact_dics = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(new_contact_dics)
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        ...
    
    def remove(self, name):
        for contact in self.contacts:
            print(self.contacts)
            if contact['name'] == name:
                self.contacts.remove(contact)
        # find the contact in self-contacts with the given name
        # remove the element at that index
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        for contact in self.contacts:
            if contact['name'] == old_name:
                self.contacts.remove(contact)
                new_contact_dics = {'name': new_name, 'phone_number': new_phone_number, 'email': new_email}
                self.contacts.append(new_contact_dics)        
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        ...
    
contact_list = ContactList() # create an instance of our class
#contact_list.load()
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