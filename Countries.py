from bs4 import BeautifulSoup
import requests
import csv

url="http://www.scrapethissite.com/pages/simple/"
response=requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# fnd all country rows instead of all rows
divs = soup.find_all("div", class_="country")


# we need an element to store info to csv
# creating a dictionary for that

countries_dict = []

# looping through the rows
for div in divs:
    country_elem = div.find("h3", class_="country-name")
    if country_elem is not None:
        country = country_elem.text.strip()
    else:
        country = ""

    capital_elem = div.find("span", class_="country-capital")
    if capital_elem is not None:
        capital = capital_elem.text.strip()
    else:
        capital = ""

    population_elem = div.find("span", class_="country-population")
    if population_elem is not None:
        population = population_elem.text.strip()
    else:
        population = ""

    area_elem = div.find("span", class_="country-area")
    if area_elem is not None:
        area = area_elem.text.strip()
    else:
        area = ""

    # printing the results
    print(country, capital, population, area)

    # adding the scraped country info to a dictionary

    countries_dict.append({
        "name": country,
        "capital": capital,
        "population": population,
        "area": area,
    })

# printing out the dictionary
print (countries_dict)

# write field names of your dictionary in the order you want them to appear in the csv
field_names = ["name", "capital", "population", "area"]

# filename for your output csv
output_filename = "country_info.csv"

# opening the file to write and setting the encoding, then writing to it using the csv library
with open (output_filename, 'w', newline='', encoding="utf-8") as f_output:
    writer = csv.DictWriter(f_output, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(countries_dict)