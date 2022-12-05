import requests


print("\n Welcome To Dad Jokes Version Two\n")
print("Come on let have fun with some jokes!!!\n")


#Add the ability to "search" for jokes using another endpoint by asking the user input.
choice = input("Please enter an animal you want a joke about!\n")


# API calls to get the jokes from the dad-joke website.
url = "https://icanhazdadjoke.com"
headers = {
    "accept": "application/json"
}

"""
Create a REPL that allows one to enter a search term
and go through jokes one at a time. 
You can also add support for multiple pages.
"""

search_url = f"https://icanhazdadjoke.com/search?term={choice}"
response = requests.get(search_url, headers = headers)
data = response.json()

results = data['results']
for x in results:
    print(x['joke'],"\n")
    break



else:
    print(f"Sorry there is no jokes for {choice} please try another animal")



















# 
# url = "https://icanhazdadjoke.com/"
# headers = {
#     "accept": "application/json"
# }

# 
# choice = input("Please enter a name of any animal you want a joke about:\n")
# search_url = f"https://icanhazdadjoke.com/search?term={choice}"

# response = requests.get(choice, headers= headers)
# print(response.text)
# data = response.json()

# results = data['results']
# for jokes in results:
#     print(jokes['joke'])

