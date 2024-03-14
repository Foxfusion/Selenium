import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "http://www.foxfusion.net"

req = requests.get(url)



page = BeautifulSoup(req.content, "html.parser")
print(page.prettify())

title = page.head
print(title.text)

all_products = [h1]

products = page.findAll("div", {"class": "_3pLy-c row"})

for product in products:
    lname = product.select("div > div._4rR01T")[0].text.strip()
    print(lname)
    price = product.select("div > div._30jeq3 ")[0].text.strip()
    print(lprice)

    all_products.append([lname, lprice])

print("record Inserted Successfully")

print(all_products)

col = ["Name", "Price"]

data = pd.DataFrame(all_products, columns=col)
print(data)

data.to_csv('extract_data.csv', index=False)