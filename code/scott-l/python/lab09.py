'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 9 - Contact List
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 7, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

'''
Let's write class for managing a contact list. 
Copy the code below into a file and fill in the functions. 
Save the following files below to your personal code folder. 
To open the file, look at the File IO doc, to parse the JSON 
into a Python dictionary, look at json module.

'''

import requests
import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
         # 2) get the text from the file
        with open('contacts.json', 'r') as contact_file:
            file_contents = contact_file.read()
       
        print(file_contents)  # DEBUG
        # 3) convert the text into a python dictionary (json.loads)
        file_contents = json.loads(file_contents)
        # 4) get the list of contacts out of the dictionary
        #print(file_contents_json.keys())  # DEBUG
        #print(file_contents_json.values())  # DEBUG
        # 5) assign the list of dictionaries to self.contacts
        self.contacts = file_contents
        print('METHOD-load')
        print(type(self.contacts))
        ...
    
    def count(self):
        # return the length of self.contacts
        contact_file = self.contacts
        print('METHOD-count')  #DEBUG
        return len(contact_file['contacts'])
        ...
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as contact_file:   
        # 2) put self.contacts in a dictionary with the key 'contacts'
          file_contents = self.contacts
        # 3) convert the dictionary to a json string (json.dumps)
          contact_file_jason = json.dumps(file_contents)
        # 4) write the json string to the file
          contact_file.write(contact_file_jason)
        print('METHOD-save')  #DEBUG
        ...

    def print(self):
        # loop over self.contacts
        file_contents = self.contacts
        # print the information for each contact on a separate line
        print('METHOD-print')  #DEBUG
        for name in file_contents['contacts']:
          print(name)
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        new_dict = dict(name = name,phone_number = phone_number, email = email)
        print(type(new_dict))
        # add the new dictionary to self.contacts
        file_contents = self.contacts
        file_contents['contacts'].update(new_dict)  ## QUESTION : WHy does this become a list when I add the contacts pointer?  prevents from updating the list
        print(file_contents)
        print('METHOD-add')  #DEBUG
        ... 
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        print('METHOD-remove')  #DEBUG
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        print('METHOD-update')  #DEBUG
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