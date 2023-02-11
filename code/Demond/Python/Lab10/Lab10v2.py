import requests
import json

#this is the input for the keyword and variable for the page
keyword = input("enter a keyword to search for quotes: ")
page = 1
test = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#this is the json dictionary
secondtest = json.loads(test.text)

#This is the page value
diction_quotes = secondtest["quotes"]

#THis is a class for the actual quotes to display
# class quotes:
#     def __init__(self):
#         x = 1

#     def print_quote(self):
#         for x in diction_quotes:
#             print(x['author' ] +" - " + x['body'])  
# y = quotes()

#this for loop will keep count of the total quotes
count = 0
for x in diction_quotes:
    count +=1

#-------------------------------------------------------------------
print(f" {count} quotes associated with {keyword} - page {page} ")
#you could also use the class I created from line 15
for x in diction_quotes:
    print(x["body"])
#-------------------------------------------------------------------

#From here my attempt is to begin a while loop dependent on the users response, also, I will be adding an integer to change the page within the while loop
response = input("enter 'next page' or 'done': ")
while response == "next page":
    if response == "done":
        print("done")
        break

    if response == "next page":
        page += 1
        test = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        #This is the page value
        secondtest = json.loads(test.text)
        diction_quotes = secondtest["quotes"]

        # #THis is a class for the actual quotes to display
        # y = quotes()
        print(f" {count} quotes associated with {keyword} - page {page} ")
        for x in diction_quotes:
            print(x["body"])
        response = input("enter 'next page' or 'done': ")