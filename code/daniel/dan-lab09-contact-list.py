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

contacts.json

{
    "contacts": [{
        "name": "Dora M. Smith",
        "phone_number": "919-781-7129",
        "email": "doramsmith@hotmail.com"
    },{
        "name": "Annette D. Berube",
        "phone_number": "662-319-6954",
        "email": "annette@gmail.com"
    },{
        "name": "Austin M. Pigott",
        "phone_number": "478-777-8878",
        "email": "austin@aol.com"
    }]
}

# lab17_contact_list.py

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        ...
    
    def count(self):
        return len(self.contacts) # return the length of self.contacts
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        ...

    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        print(*self.contacts, sep = '\n')
        ##### May display in dictionary format...

    def add(self, name, phone_number, email):
        contact = { # create a new dictionary using the 3 parameters
            'name': name,
            'phone_number': phone_number,
            'email': email
            }
        self.contacts.add(contact) # add the new dictionary to self.contacts
    
    def remove(self, name):
        # find the contact in self.contacts with the given name
        if name in self.contacts:
        # self.contacts.find(name)
        # remove the element at that index
        
        
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        ...
    
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