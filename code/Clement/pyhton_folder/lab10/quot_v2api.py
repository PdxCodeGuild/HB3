import json
import requests
# import pprint


url = "https://favqs.com/api/qotd"
headers = {
    "accept": "application/json"
}

keyword = input("Please enter a keyword to search for quotes:\n")
page = input("enter 'next page' or 'done':\n")

search_key_page = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
response = requests.get(search_key_page, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

page_count = 0
data = response.json()
print(data)

for key in data:
    pass
    # print(data[key])
    # print(key[last_page])
    # print(key[quotes])



    # results =(data[page])
    # print(results)

# p = pprint.PrettyPrinter(width=1)
# print(response.text)
# results = data['page']

# print(type(results['quotes']))

# for quote in results:
#     print("\n=============================================================\n")
#     print(quote['quotes'], quote['author'])
#     print("\n=============================================================\n")