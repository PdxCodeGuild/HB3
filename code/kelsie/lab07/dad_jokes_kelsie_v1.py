import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

data = response.json()

<<<<<<< HEAD
<<<<<<< HEAD
print(data.get('joke'))
=======
print(data.get('joke')) 
>>>>>>> fd85668df04aa1ca7e5a93e91d88939eba9730da
=======

print(data.get('joke'))

>>>>>>> 8735dd1a338782c9a7e4afb818e1fcc0f26ff8aa
