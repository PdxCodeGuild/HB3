import json


class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):

        with open('contacts.json', 'r') as f: # 1) open 'contacts.json' with option 'r' for read
            contents = f.read() # 2) get the text from the file
            data = json.loads(contents) # 3) convert the text into a python dictionary (json.loads)
        for contact in data['contacts']: # 4) get the list of contacts out of the dictionary
            self.contacts.append(contact) # 5) assign the list of dictionaries to self.contacts
        
       
    
    def count(self):
        return len(self.contacts) # return the length of self.contacts
        
    
    def save(self):
        with open('contacts.json', 'w') as f: # 1) open 'contacts.json' with open 'w' for write
            contact_dict = {'contacts':self.contacts} # 2) put self.contacts in a dictionary with the key 'contacts'
            json_string = json.dumps(contact_dict) # 3) convert the dictionary to a json string (json.dumps)
            f.write(json_string) # 4) write the json string to the file

    def print(self):
        for contact in self.contacts: # loop over self.contacts
            print(contact) # print the information for each contact on a separate line

    def add(self, name, phone_number, email):
        self.new_contact = {'name': name, 'phone_number':phone_number, 'email':email} # create a new dictionary using the 3 parameters
        self.contacts.append(self.new_contact)# add the new dictionary to self.contacts
    
    def remove(self, name):
        for contact in self.contacts: # find the contact in self-contacts with the given name
            if contact['name'] == name:
                self.contacts.remove(contact) # remove the element at that index
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        for contact in self.contacts: # find the contact in self.contacts with the given old_name
            if contact['name'] == old_name:
                ContactList.add(self, new_name, new_phone_number, new_email)
        # set that contacts' name, phone number, etc to the given values
        ...
    
contact_list = ContactList() # create an instance of our class
# contact_list.load()
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