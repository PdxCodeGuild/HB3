import requests 

# I have imported the requests module
print("\n Welcome To Dad Jokes\n")
print("\nCome on let have fun with some jokes!!!\n")

# This will call the URL variable using our requests module
url = "https://icanhazdadjoke.com/"
headers = {"accept": "application/json"}

# the resonse will access the website and then accept a joke from the site
response = requests.get(url = url, headers = headers)

#response will then be stored as a text file and printed with the joke
data = response.json()
result = (data['joke'])

print(result)