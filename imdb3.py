#!/usr/bin/env python
# coding: utf-8

# # Saving Data to CSV and Excel

# In[7]:


import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv


# In[8]:

# The file name where the information
filename = 'imdb.csv'
f = open(filename,'w',newline = '')
music = csv.writer(f)
# CSV Writter

# The file url that will be scraped
html = urlopen('http://www.imdb.com/chart/top/')
bsobj = soup(html.read())
xl = []
#Iterating over movies to extreact
# each movie details
for index in range(0, len(movies)):

    # Seperating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append9(data)

# printing movie details with its ratings
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
          ') -',  'Starring:', movie['star-cast' ], movie['rating'])






print(movie)


# In[6]:


import os
os.getcwd()


# In[9]:


xl
:

# In[9]:


xl


# ## Creating pandas dataframe and saving to excel

# In[10]:


import pandas as pd
df = pd.DataFrame(data = xl)
df


# In[11]:

# World Music spreadsheet
df.to_excel('imdb.cdv', index=False,header = False)


# Messag thta the scrape completed successfully
print('Spreadsheet saved.')


