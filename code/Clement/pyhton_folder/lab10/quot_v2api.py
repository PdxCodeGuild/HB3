import requests

# API calls by using requests library
url = "https://favqs.com/api/qotd"
headers = {
    "accept": "application/json"
}

# Asking for the user input 
keyword = input("Please enter a keyword to search for quotes:\n").lower()
page = 1

while keyword:
    search_key_page = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
    response = requests.get(search_key_page, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    # p = pprint.PrettyPrinter(width=80)
    # Accessing nested dictionary keys from json file
    data = response.json()
    results = data['quotes']
    for x in results:
        print(x['body'],"\n","\x1B"+x['author']+"\x1B")
        print("===========================================================\n")

    # Getting next sets of quotes from next page
    next_page = input("Enter 'next' to next page or 'done' to quick:\n").lower()
    if next_page == "next":
        page +=1

    # Exit point from while loop
    elif next_page == "done":
            break
            


    else:
        print(f"Sorry there is no quotes for {keyword} please try another animal")
