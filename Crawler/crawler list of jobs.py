__author__ = "Spyros Ntouroukis"
__copyright__ = "Copyright 2019, Crawler"
__version__ = "1.0.1"
__maintainer__ = "Spyros Ntouroukis"
__email__ = "spyros-ntouroukis@hotmail.com"
__script_infos__ = "This is the part to crawl page number from kariera site"
import requests
import re
from requests import get
import requests
from bs4 import BeautifulSoup
import time


print("------------------------ Script just started ------------------------")
#initializing the page
url = 'https://www.kariera.gr/θέσεις-εργασίας?q='
q='a'  # change your q here
response = get(url +str(q))
#print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
#type(html_soup)

#here we removing styles and scripts
for script in html_soup(["script", "style"]):
    script.extract()

print("------------------------ javascripts and style removed ------------------------")

#here we start crawl the area of content we need
page_number = html_soup.find_all('div', class_="bloc clear center")
job = page_number[0].find_all("a")
#print(job[5].text)

# store to int the value we got from the page , for number of pages from the site
a= int(str(job[5].text))
#print(type(a))
c=[] # we initialize value to store all urls


print("------------------------ Q page numbers Crawled, storing pages ------------------------")
# get all pages
for page in range(1 ,a+1):
    #sec=0.5
    #time.sleep(sec)
    str(page)
    c.append(url + str(page) + '&q=' +str(q))    # on c we store all the queried pages
    #r = requests.get(url + str(page) + '&q=it')
   # print(r.text)


print("------------------------ Printing stored pages ------------------------")
for i in range(1,a):
    print(c[i])
