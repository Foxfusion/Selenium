import requests
import csv
from bs4 import BeautifulSoup


website = requests.get('https://www.imdb.com/chart/top') .text#getting HTML through request
#soup = BeautifulSoup(website, 'html.parser') #Parsing  content using Beatiful Soup

soup = BeautifulSoup(website, 'lxml')


table = soup.select("table")
table_rows = table.find_all()


data = []

for tr in table_rows:
    td= tr.find_all()
    rows= [i.text for i in td]
    data.append(rows)

with open('imdbtop.csv', 'w', newline=' ') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Data has been saved to CSV file successfully")
