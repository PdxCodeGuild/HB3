import requests

def getter():
    quotes_request = requests.get('https://favqs.com/api/qotd', headers={'accept': 'application/json'})
    quotes = quotes_request.json()
    return quotes

def parse(quotes):
    author = quotes['quote']['author']
    body = quotes['quote']['body']
    return author, body 

def main(author, body):
    print(f"{body}\n{author}")

main(*parse(getter()))