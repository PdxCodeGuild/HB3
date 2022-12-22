import requests 
import json

#filter = 
# page = 1
#Find base url 
#Find end point 
#grab request  -----  r = request.get(baseurl + endpoint)
# response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

# data = response.json()


# # #body , id , url, author, pages
# # # print(response)---- Helps check our code
# quote = data.get('quote').get('body')
# author = data.get('quote').get('author')
# print(quote)
# print(author)

#------------------------------------------------------- VERSION 2 ----------------------------------------
#Step 1 Grab URL
#Step 2 Ask user for input
#Step 3 Use loop to continue running quotes until told to stop
#Step 3 Get the next pages quotes
#Step 4 End loop
keyword = input('enter a keyword to search for quotes:')
page = 1



response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}',
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
data = response.json()
for key in data['quotes']:
    print(key['body'])
print(page)
next_page = input("enter 'next page' or 'done': ")
while next_page:
    if next_page == 'next page':
        page += 1
        response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}',
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = response.json()
        for key in data['quotes']:
            print(key['body'])
        print(page)
        next_page = input("enter 'next page' or 'done': ")
    elif next_page == 'done':
        print('done')  
        break
    
    

    # quote = data.get('quote').get('body')
    # author = data.get('quote').get('author')

    # next_page = input("enter 'next page' or 'done': ")
    # if page == 'next page':
    #     page += 1 
    # elif page == 'done':
    #     break


# page = input("enter 'next page' or 'done': ")
# #Pages = 1 + next page
