import json
class ContactList:
    
    def __init__(self):
        self.contacts = []
        

    def load(self):
        file = open('contacts.json', 'r')
        data = json.loads(file.read())
        dictionaries = data['contacts']
        self.contacts = dictionaries
            
   
    def count(self):
            return len(self.contacts)

  
    def save(self): 
        self_dict = {}
        self_dict.update({'contacts' : self.contacts})
        with open('contacts.json' , 'w') as file :
            saved = json.dumps(self_dict)
            file.write(saved)
            file.close()
        
        
    def print(self): 
        for x in range(len(self.contacts)) :
            print(self.contacts[x]['name'])
            print(self.contacts[x]['phone_number'])
            print(self.contacts[x]['email'])
            print(" ")
        

    def add(self, name, phone_number, email):
        new_contact = {
               'name' : name ,
                'phone_number' : phone_number ,
                'email' : email
                }
        self.contacts.append(new_contact)
        print(self.contacts)

        
    def remove(self, name):
        for x in range(len(self.contacts)) :
            if self.contacts[x]['name'] == name :
                del self.contacts[x]
                break
        
  
    def update(self, old_name, new_name, new_phone_number, new_email):
        for x in range(len(self.contacts)) :
            if self.contacts[x]['name'] == old_name :
               self.contacts[x]['name'] = new_name
               self.contacts[x]['phone_number'] = new_phone_number
               self.contacts[x]['email'] = new_email




contact_list = ContactList() 
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
