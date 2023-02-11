import requests


url = " https://favqs.com/api/qotd"

headers = {
    "accept": "application/json"
}

response = requests.get(url = url, headers = headers)

data = response.json()

result = data['quote']
print("\n=============================================================\n")
print(result['body'],"\n","\x1B"+ result['author']+"\x1B")
print("\n=============================================================\n")
