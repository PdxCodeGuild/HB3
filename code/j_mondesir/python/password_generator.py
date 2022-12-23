# Import two modules random and string
import random
import string 
import requests
import os
import datetime 

letters = string.ascii_letters
digit = string.digits
punctuation = string.punctuation
number = letters + digit + punctuation

        
# Function to create password    
def create(num_len):
    file_path = r'pass_list.txt'
    password = ''
    #store_pass = []
    for x in range(num_len) :
        password += ''.join(random.choice(number))
        #store_pass.append(password)
    if os.path.exists(file_path):
        with open(file_path,'a') as fp:
            fp.write(str('\t'+password+'\n'))
            fp.write(datetime.datetime.now().ctime())
    else:
        with open('pass_list.txt', 'w') as fp:
            fp.write(str('\t'+password+'\n'))
            fp.write(datetime.datetime.now().ctime())
    return password
                
# Funtion to list all save password
def list_p():
    with open('pass_list.txt', 'r') as fp:
        read_file = fp.read()
        return read_file
               
# Ask for user input for length of paswword
print('Welcome to Password Generator!')
print()
print(
    '''
    PLEASE CHOOSE ONE THE OPETIONS
      1. Create a password
      2. List your password
      3. Check if your password is compromise
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
        
        
        
        

