import requests
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) # params={'format': 'json'})

# load the response in the variable
jresponse = json.loads(response.text)

#this is the input for the keyword and variable for the page
keyword = input("enter a keyword to search for quotes: ")
page = 1
test = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#this is the json dictionary
secondtest = json.loads(test.text)

#This is the page value
page = secondtest['page']
diction_quotes = secondtest["quotes"]

#THis is a class for the actual quotes to display
class quotes:

    def __init__(self):
        x = 1

    def print_quote(self):
        for x in diction_quotes:
            print(x['author' ] +" - " + x['body'])  
y = quotes()

#this for loop will keep count of the total quotes
count = 0
for x in diction_quotes:
    count +=1

#-------------------------------------------------------------------
print(f" {count} quotes associated with {keyword} - page {page} ")
print(y.print_quote())
#-------------------------------------------------------------------

#From here my attempt is to begin a while loop dependent on the users response, also, I will be adding an integer to change the page within the while loop
while response == input("enter 'next page' or 'done': "):
    if response == ("done"):
        print("done")
        break

    if response == "next page":

        response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) # params={'format': 'json'})

        jresponse = json.loads(response.text)

        keyword = input("enter a keyword to search for quotes: ")
    
        test = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    
        
        
    class quotes:
        page + 1
        def __init__(self):
            x = 1

    def print_quote(self):
        for x in diction_quotes:
            print(x['author' ] +" - " + x['body'])  
    y = quotes()
for x in diction_quotes:
    count +=1

    
#-------------------------------------------------------------------
print(f" {count} quotes associated with {keyword} - page {page} ")
print(y.print_quote())
#-------------------------------------------------------------------