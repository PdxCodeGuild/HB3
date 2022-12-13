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
from operator import itemgetter

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        print('METHOD-load')  # DEBUG
        # 1) open 'contacts.json' with option 'r' for read
         # 2) get the text from the file
        with open('contacts.json', 'r') as contact_file:
            file_contents = contact_file.read()
        # 3) convert the text into a python dictionary (json.loads)
        print(f'The file contents read is {type(file_contents)}')  # DEBUG
        file_contents1 = json.loads(file_contents)  # loads the file from the JSON string format into a list format
        print(f'The file contents after Json Load {type(file_contents1)}')  # DEBUG
        # print(file_contents)  # DEBUG
        # 4) get the list of contacts out of the dictionary  << START HERE need to understand how to extract the lists from the dictionary key "contacts"
        # dictionary_keys = file_contents1.keys()  # DEBUG
        # print(f'The dictionary keys are {dictionary_keys}')  # DEBUG
        contact_list = file_contents1['contacts']
        print(f'The file contents after list key {type(contact_list)}')
        # 5) assign the list of dictionaries to self.contacts
        self.contacts = contact_list
       
        # print(type(self.contacts))  # DEBUG
        print(self.contacts)
        # print(self.contacts[0]["name"])  # DEBUG
        ...
    
    def count(self):
        # return the length of self.contacts
        contact_file = self.contacts
        print('METHOD-count')  #DEBUG
        return len(contact_file)
        ...
    
    def save(self):
        print('METHOD-save')  #DEBUG
        file_contents_dict = {} # create an empty dictionary
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as contact_file:   
        # 2) put self.contacts in a dictionary with the key 'contacts'
            print(f'This is the contacts list {self.contacts}')  # DEBUG
            file_contents_dict["contacts"] = self.contacts  
            print(f'This is the dictionary self contacts with key {file_contents_dict}') # DEBUG
        # 3) convert the dictionary to a json string (json.dumps)
            contact_file_json = json.dumps(file_contents_dict)
        # 4) write the json string to the file
            print(type(contact_file_json))  # DEBUG
            contact_file.write(contact_file_json)
        
        ...

    def print(self):
        # loop over self.contacts
        file_contents = self.contacts
        # print the information for each contact on a separate line
        # print(f'The type for print file_contents is {type(file_contents)}')  # DEBUG
        # print('METHOD-print')  #DEBUG
        
        # iterate over the list and print to screen
        for print_list in file_contents:
            # now j is a dict, now we see the keys
            # of the dict
            for key in print_list.keys():
                # print every key of each dictionary
                print(f'{key} :  {print_list[key]}')
            # end for
            print("--------------------------------")
        # end for
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        new_dict = dict(name = name,phone_number = phone_number, email = email)
        # print(type(new_dict))  # DEBUG
        # add the new dictionary to self.contacts
        file_contents = self.contacts
        file_contents.append(new_dict)  # Add the new dictionary information to the list of dictionaries
        print(file_contents)  # DEBUG
        print('METHOD-add')  #DEBUG
        ... 
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        print('METHOD-remove')  #DEBUG

        # search the list of dictionaries for the element where the 'name' key 
        # is equal to the input name of function using the fiter function with a 
        # lamda function.  Use the filter() function to search for the values that 
        # mathc the lambda function and then finally use the list() function to convert
        # the results into a list
        # print(list(filter(lambda person: person['name'] == name,self.contacts)))
        # find the items index in a list of Dictionaries, using the next and enumerate function to search
        # and find the items index
        # print(next((i for i, x in enumerate(self.contacts) if x["name"] == name), None))

    
        for index in range(len(self.contacts)):
            # if the contacts list starts with the input name string then 
            if self.contacts[index]["name"].startswith(name):
                # print(True) # EEBUG
                # confirm with user if they want to delete the name
                remove_request = input(f'''Do you want to Remove this name from the list? (y,n)
                 {self.contacts[index]} ''')
                if remove_request == 'y':
                    # print(f'the index is {index}') # DEBUG
                    del self.contacts[index]
                    print(f'Name Record Removed from List')
                    break
                elif remove_request == 'n':
                    print(f'exit - no changes made')
                    break
                # end if
            else:
                # print(False)  # Debug
                print('Name record not found - please type the name again')
                break
            # end if
        
        # end for


        # if name in self.contacts:
        #     print(str(name) +  ' is inside the list')
        # else:
        #     print(str(name)  + ' is not present in the list')

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