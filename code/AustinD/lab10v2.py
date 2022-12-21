import requests
import json

def get_quotes(page, keyword):
  url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
  quotes_request = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'accept': 'application/json'})
  quotes = quotes_request.json()
  return quotes

def parse_quotes(quotes):
  author = quotes['author']
  body = quotes['body']
  return author, body

def main():
  page = 1
  keyword = input("Enter a keyword:")
  quotes = get_quotes(page, keyword)

  while True:
    for quote in quotes['quotes']:
      author, body = parse_quotes(quote)
      print(f"{body}\n{author}")

    next_page = input("Enter 'next page' or 'done':")
    if next_page.lower() == 'done':
      keyword = input("Enter a new keyword:")
      page = 1
      quotes = get_quotes(page, keyword)
    else:
      page += 1
      quotes = get_quotes(page, keyword)

main()