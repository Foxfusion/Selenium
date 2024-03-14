import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


# In[27]:


my_url = 'https://www.imdb.com/list/ls053501318/'
#opening up connection, downloading the page
imdb = urlopen(my_url)

#html parsing
bsobj = soup(imdb.read(),'html.parser')

#grabs each star
containers =  bsobj.findAll('div',{'class':'lister-item mode-detail'})
pic = bsobj.findAll('img')


for container,img in zip(containers,pic):
    name = container.h3.a.text.strip()

    image = img.get('src')
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(image, full_name)


import os
os.getcwd()