import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

data = response.json()

<<<<<<< HEAD
print(data.get('joke'))
=======
print(data.get('joke')) 
>>>>>>> fd85668df04aa1ca7e5a93e91d88939eba9730da
