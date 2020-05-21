import requests
from bs4 import BeautifulSoup

URL = 'https://github.com/'
page = requests.get(URL)
soup =BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())