import re
from requests import get
import requests
from bs4 import BeautifulSoup
import time



url = 'https://www.kariera.gr/θέσεις-εργασίας?pg='
response = get(url)
print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
#type(html_soup)
for script in html_soup(["script", "style"]):
    script.extract()#removing styles and scripts

c=[] # we initialize value to store all urls
# get all pages
q='it'  # change your q here
for page in range(1 ,400):
    sec=0.5
    time.sleep(sec)
    str(page)
    c.append(url + str(page) + '&q=' +str(q))    # on c we store all the queried pages
    #r = requests.get(url + str(page) + '&q=it')
   # print(r.text)

print(c)

#page_number = html_soup.find_all('div', class_="bloc clear center")
#job = page_number[0].find("span", {'class': 'ellipsis'})
#for span_tag in job[0].find_all('span'):
 #   span_tag.replace_with('')
#print("Τίτλος Δουλειάς",job[0].text.strip())
#print("Εταιρία:", span_tag.text)
#print(job.text)
