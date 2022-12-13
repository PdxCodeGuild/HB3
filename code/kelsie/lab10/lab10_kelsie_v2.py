import requests

keyword = input("What word would you like to search for? ")
search = ('https://favqs.com/api/quotes?page=<page>&filter=')

search_response = requests.get(search + keyword ,  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quote_dict = {}     

quote_dict.update(search_response.json())


for quote in quote_dict :
    quotes = (quote_dict.get('quotes'))

    
