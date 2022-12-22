# Import two modules random and string
import random
import string 
import requests

# Ask for user input for length of paswword
print('Welcome to Password Generator!')
print()
user = int(input('Enter password lenght: '))

# Declare variables to create password
letters = string.ascii_letters
digit = string.digits
punctuation = string.punctuation
number = letters + digit + punctuation
password = []

# create while to create random password
while len(password) != user :
    password.append(random.choice(number))
    
final = ''.join(password)
    
# print password to user
print()
print(f'Your password is:\n> {final}')