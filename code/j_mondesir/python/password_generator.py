# Import two modules random and string
import random
import string 
import requests
import os
from datetime import datetime
import hashlib
import json

letters = string.ascii_letters
digit = string.digits
punctuation = string.punctuation
number = letters + digit + punctuation

        
# Function to create password    
def create(num_len):
    file_path = r'pass_list.txt'
    password = ''
    now = datetime.now()
    for x in range(num_len) :
        password += ''.join(random.choice(number))
        
    if os.path.exists(file_path):
        with open(file_path,'a') as fp:
            fp.write(now.strftime("%d/%m/%Y")+'\t'+str(password)+'\n')
            
    else:
        with open('pass_list.txt', 'w') as fp:
            fp.write(now.strftime("%d/%m/%Y")+'\t'+str(password+'\n'))
        
    return password
                
# Funtion to list all save password
def list_p():
    with open('pass_list.txt', 'r') as fp:
        read_file = fp.read()
        return read_file


def check_pass(first_5_hash):
    url = "https://api.pwnedpasswords.com/range/"+first_5_hash
    payload={}

    response = requests.request("GET", url, data=payload)
    resp_json = json.dumps(response.text)
    resp_dict = json.loads(resp_json)
    return resp_dict

# Function to hash password to sha1
def pass_encryp(ur_pass):
    hash_1 = hashlib.sha1(ur_pass.encode())  
    return hash_1.hexdigest()
            
# Ask for user input for length of paswword
print('Welcome to Password Generator!')
print()
print(
    '''
    PLEASE CHOOSE ONE THE OPETIONS
      1. Create a password
      2. List your password
      3. Check if your password 
      4. Hash your password
      5. Exit
      '''
      )

while True:
    user_choice = input('Enter an option:\n> ')
    if user_choice == 'Create':
        num_len = int(input('What is the length of the password:\n> '))
        print(create(num_len))
    elif user_choice == 'List':
        print(list_p())
    elif user_choice == 'Check':
        first_5_hash = input('Enter the first 5 characters of a SHA-1 password:\n> ')
        print(check_pass(first_5_hash))        
    elif user_choice == 'Hash':
        ur_pass = input('Enter the password you want to hash:\n> ')
        print(pass_encryp(ur_pass))
    elif user_choice == 'Exit':
        break
print('Thank you! for using Password Generator')
    
        
        
        
        

