__author__ = "Spyros Ntouroukis"
__version__ = "1.0.1"
__maintainer__ = "Spyros Ntouroukis"
__email__ = "spyros-ntouroukis@hotmail.com"
__script_infos__ = "This is the part to crawl page number from kariera site"

import re
from requests import get
import requests
from bs4 import BeautifulSoup
import json
from time import sleep


print("------------------------ Script just started ------------------------")

#initializing the page
domain = 'https://www.kariera.gr'
url = 'https://www.kariera.gr/θέσεις-εργασίας'
q='it'  # change your q here future improvement to ask user to enter q keyword
response = get(url + '?q=' +str(q))

#print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
#type(html_soup)

#remove styles and scripts
for script in html_soup(["script", "style"]):
    script.extract()
print("------------------------ javascripts and style removed ------------------------")

#find the page number to crawl content for it
page_number = html_soup.find_all('div', class_="bloc clear center")
job = page_number[0].find_all("a")
#print(job[5].text)
# store to int the value we got from the page , for number of pages from the site
a= int(str(job[5].text))

c=[] # initialize value to store all urls
print("------------------------ Q page numbers Crawled, storing pages ------------------------")
# get all pages
for page in range(1 ,a+1):
    #sec=0.5
    #time.sleep(sec)
    str(page)
    c.append(url+ '?pg=' + str(page) + '&q=' +str(q))    # on c store all the queried pages
    #r = requests.get(url + str(page) + '&q=it')
   # print(r.text)
print("------------------------ Store pages & crawl from each page job pages ------------------------")
append_links=[]
for i in range(0,a):
    pattern = re.compile("^(/)")
    #print(c[i])
    #jobsurl= c[i]
    response = get(c[i])
    jobsurl = BeautifulSoup(response.text, 'html.parser')
    #contecntjob = jobsurl.find_all('div', class_="jobs-content")
    contecntjob = jobsurl.find_all('div', class_="job")
    contecntjob_link = jobsurl.find_all('a', class_="job-title", href=pattern)
    for link in contecntjob_link:
        if link.has_attr('href'):
            link_c = domain+link.attrs['href']
            append_links.append(link_c)
        #future improvement here to encode




print("------------------------ crawle jobs per page ------------------------")

# this part crawl the job page

for i in range(len(append_links)):
    url = append_links[i]
    response = get(url)
    #print(response.text[:500])

    from bs4 import BeautifulSoup
    not_crawled_pages=[]
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    for script in html_soup(["script", "style"]):
        script.extract()  # removing styles and scripts
    text = html_soup.find_all('div', class_="col-2 small full-mobile")
    if len(text)==0:
        print("Can;t crawl this page yet , we need to customize code to crawl this page :",url)
        not_crawled_pages.append(url)

    else:
        job = text[0].find_all("div", {'class': 'bloc clear nm col-2 small-marge'})
        for span_tag in job[0].find_all('span'):
            span_tag.replace_with('')
        print("Τίτλος Δουλειάς", job[0].text.strip())
        print("Εταιρία:", span_tag.text)
        apasxolisi = html_soup.find_all('div', class_="snapshot")
        news_content = apasxolisi[0].find_all("div", {'class': 'snapshot-item'})
        list = []

        for wrapper in apasxolisi[0].find_all("div", {'class': 'snapshot-item'}):
            list.append(wrapper.text)
            # print(wrapper.text)
        print("Απασχοληση:", list[0].strip())
        print("Περιοχή:", list[1].strip())

        perigrafi = html_soup.find('div', class_="bloc")
        list2 = []
        for wrapper in perigrafi.find_all("div", {'id': 'job-description'}):
            list2.append(wrapper.text)
        # news_content1 = perigrafi.find("div",{'id': 'job-description'})
        # print(news_content.text)
        # print(news_content1.text)
        print(list2[0].replace("\n", ""))
        kodikos = perigrafi.find("div", {'id': 'job-id'})
        for h3_tag in kodikos.find('h3'):
            h3_tag.replace_with('')
        print(h3_tag, ":", kodikos.text.replace("\n", ""))


print("------------------------ Save to Json file ------------------------")

#This part store domain information and crawled urls of the q
crawler_json = { "Page informations": {'Domain': domain,'Q': q,'Number Of Pages': a , 'Crawled Urls': append_links,'Not crawled Urls':not_crawled_pages}}

with open('Data.json', 'w') as json_file:
    json.dump(crawler_json , json_file)

# this part stores to json the crawled job data from each page , not finished yet
#with open('jobdata.json', mode='w', encoding='utf-8') as f:
#    json.dump([], f)
#jobdata_crawl = { "Job informations": {'url': url,'Τίτλος Δουλειάς': job[0].text.strip(),'Εταιρία:': span_tag.text , 'Απασχοληση': list[0].strip(),'Περιοχή': list[1].strip(),'kodikos thesis': kodikos.text.replace("\n", "") }}

#with open('jobdata.json', 'w') as json_file:
#    json.dump(jobdata_crawl , json_file)




print("------------------------ Store to MySql Database ------------------------")
#this part of the code stores data to database.

