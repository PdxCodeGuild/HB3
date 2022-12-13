import requests
print("\n Welcome To Dad Jokes\n")
print("\nCome on let have fun with some jokes!!!\n")

# API calls to get the jokes from the dad-joke website.
url = "https://icanhazdadjoke.com/"
headers = {
    "accept": "application/json"
}

response = requests.get(url= url, headers= headers)

data = response.json()
result = (data['joke'])

print(result)