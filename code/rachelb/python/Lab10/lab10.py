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

#------------------------------------VR 2 -------------------
#Step 1 Grab URL
#Step 2 Ask user for input
#Step 3 Use loop to continue running quotes until told to stop
#Step 3 Get the next pages quotes
#Step 4 End loop
keyword = input('enter a keyword to search for quotes:')
page = 1


while keyword == input :
    if True
    response = requests.get(f'https://favqs.com/api/quotes?page={page}>&filter=<{keyword}>',
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    
    data = response.json()


print(data)
    
    # quote = data.get('quote').get('body')
    # author = data.get('quote').get('author')

    # quotes = len(data['quote'])
    # print(quotes)

    # page = input("enter 'next page' or 'done': ")
    # if page == 'next page':
    #     page += 1 
    # elif page == 'done':
    #     break


    
# length = len(data['quotes'])

# next_page = 1

# while next_page == 'done':




# page = input("enter 'next page' or 'done': ")
# #Pages = 1 + next page
