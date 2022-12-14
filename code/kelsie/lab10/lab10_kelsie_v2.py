import requests

page = 1
quote_search = 'Y'
keyword = input("What keyword would you like to search for? ")

while quote_search == 'Y' :

    search = (f'https://favqs.com/api/quotes?page={page}&filter=')

    search_response = requests.get(search + keyword ,  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    quote_dict = {}     

    quote_dict.update(search_response.json())

    for quotes in quote_dict :
        quotes = (quote_dict.get('quotes'))
        for index in quotes :
            print(index['body'] + ' - ' + index['author'])
        break
    
    next_page = input("Would you like to go to the next page? Y/N: ")
    if next_page == 'Y' :
        page += 1
        quote_search == 'Y'

    elif next_page == 'N' :
        quote_search = input("Would you like to search for a new keyword? Y/N: ")
        if quote_search == 'N' :
            print("Thanks for playing!")
            break
        
    
    