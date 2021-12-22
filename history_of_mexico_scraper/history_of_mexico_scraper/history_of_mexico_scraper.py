import requests
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

from bs4 import BeautifulSoup

page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())

results = soup.find_all(title='Wikipedia:Citation needed')
print(len(results))