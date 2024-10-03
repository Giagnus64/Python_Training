from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.example.com')


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('h1').string)
