import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page  = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

print (page.text)