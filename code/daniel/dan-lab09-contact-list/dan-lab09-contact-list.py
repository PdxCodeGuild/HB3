#---------------------------------
# PDX Code Guild: HB3
# Lab09: Contact List App
# Author: Daniel Smith
# Date: 2022.12.5
#---------------------------------

# Lab 09: Contact List
# Write class for managing a contact list.
# Copy the code below into a file and fill in the functions.
# Save the following files below to your personal code folder.
# To open the file, look at the File IO doc,
# to parse the JSON into a Python dictionary, look at json module.

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open('contacts.json', 'r') as contacts_file:
            # 2) get the text from the file
            contacts_str = contacts_file.read()
            # 3) convert the text into a python dictionary (json.loads)
            from json import loads
            contacts_dict = loads(contacts_str)
            # 4) get the list of contacts out of the dictionary
            contacts = contacts_dict['contacts']
            # 5) assign the list of dictionaries to self.contacts
            self.contacts = contacts
    
    def count(self):
        # return the length of self.contacts
        return len(self.contacts)
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as contacts_file:
            # 2) put self.contacts in a dictionary with the key 'contacts'
            contacts_dict = {'contacts': self.contacts}
            # 3) convert the dictionary to a json string (json.dumps)
            from json import dumps
            contacts_str = dumps(contacts_dict)
            # 4) write the json string to the file
            contacts_file.write(contacts_str)

    def print(self):
        # loop over self.contacts and print the information for each contact on a separate line
        print(*self.contacts, sep = '\n')
        # for i in self.contacts:
        #     print(i)
        ##### Displays in dictionary format...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        i = {
            'name': name,
            'phone_number': phone_number,
            'email': email
            }
        # add the new dictionary to self.contacts
        self.contacts.append(i) 
        
    def remove(self, name):
        # find the contact in self.contacts with the given name
        for i in self.contacts:
            # remove the element at that index
            if i['name'] == name:
                self.contacts.remove(i)
        
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        for i in self.contacts:
            if i['name'] == old_name:
                # set that contacts' name, phone number, etc to the given values
                self.contacts[i] = {
                    'name': new_name,
                    'phone_number': new_phone_number,
                    'email': new_email
                }
    
contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count()} contacts.')
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