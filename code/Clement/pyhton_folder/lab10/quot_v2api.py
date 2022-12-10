import json
import requests
import pprint


url = "https://favqs.com/api/qotd"
headers = {
    "accept": "application/json"
}

keyword = input("Please enter a keyword to search for quotes:\n")
page = input("enter 'next page' or 'done':\n")

search_key_page = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
response = requests.get(search_key_page, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

page_count = 0
p = pprint.PrettyPrinter(width=80)
data = response.json()
# p.pprint(type(data))
results = data['quotes']
for x in results:
    p.pprint(x['body'])











#     print(x[data],"\n")
#     break



# else:
    # print(f"Sorry there is no jokes for {search_key_page} please try another animal")



    # print(data[key])
    # print(key[last_page])
    # print(key[quotes])



    # results =(data[page])
    # print(results)

# print(response.text)
# results = data['page']

# print(type(results['quotes']))

# for quote in results:
#     print("\n=============================================================\n")
#     print(quote['quotes'], quote['author'])
#     print("\n=============================================================\n")