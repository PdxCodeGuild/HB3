import json

#  create an instance of our class
class ContactList:
    def __init__(self):
        self.contacts = []

        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
    def load(self):
        f = open("contacts.json")
        contents = f.read()
        contents = json.loads(contents)
        self.contents = contents['contacts']
    

    # return the length of self.contacts
    def count(self):
        return len(self.contents)


        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
    def save(self):
        with open('contacts.json', 'w') as list:
            contact_dict = {'contacts': self.contacts}
            j_contacts = json.dumps(contact_dict)
            list.write(j_contacts) 


        # loop over self.contacts and print the information
        # for each contact on a separate line
    def print(self):
        for content in self.contacts:
            print(content)


        # create a new dictionary using the 3 parameters, & 
        # add the new dictionary to self.contacts
    def add(self, name, phone_number, email):
        c_new_dict = {
            "name": name,
            "phone_number": phone_number,
            "email": email
        }
        self.contacts.append(c_new_dict)
        print(self.contacts)

    
        # find the contact in self-contacts with the given name
        # remove the element at that index
    def remove(self, name):
        for index, entry in enumerate(self.contacts):
            if entry['name'] == name:
                print(name)
                del self.contacts[index]
                break
    

        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
    def update(self, old_name, new_name, new_phone_number, new_email):
        for index, entry in enumerate(self.contacts):
           if entry['name'] == old_name:
            update_dict = {
                'name': new_name,
                'phone_number': new_phone_number,
                'email': new_email,            
                } 
            self.contacts[index].update(update_dict)
            
    
contact_list = ContactList() 
contact_list.load()
print('\nWelcome To The Contacts List App (CLA)\n')
while True:
    command = input("Please enter a command or type 'help' to get the available commands:\n").lower()


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
        name = input('Name: ').title()
        phone_number = input('Phone Number: ')
        email = input('Email: ').lower()
        contact_list.add(name, phone_number, email)


    elif command == 'remove':
        name = input('Name of contact to remove: ').title()
        contact_list.remove(name)


    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ').title()
        new_name = input('New Name: ').title()
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ').lower()
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    
    
    elif command == 'help':
        print("\n===================================================")
        print('These Are The Available Commands:\nUpdate  = update a contact\nRemove  = remove a contact\nExit    = exit the program\nAdd     = add a new contact\nPrint   = print all contacts\nSave    = save contacts to a file\nLoad    = load all contacts from the file')
        print("\n===================================================")
  

    elif command == 'exit':
        break
    else:
        print('Command not recognized')