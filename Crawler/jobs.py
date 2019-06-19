from requests import get
#url = 'https://www.kariera.gr/θέση-εργασίας/junior-system-administrator-j2y0pt61dz2fbky6yz6?ipath=INTLMRCJ'
url = 'https://www.kariera.gr/θέση-εργασίας/καθηγητής-πληροφορικής-jdh8gc5w416bjstwcmh'
response = get(url)
print(response.text[:500])

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

for script in html_soup(["script", "style"]):
    script.extract()#removing styles and scripts


text = html_soup.find_all('div', class_="col-2 small full-mobile")
job = text[0].find_all("div", {'class': 'bloc clear nm col-2 small-marge'})
for span_tag in job[0].find_all('span'):
    span_tag.replace_with('')
print("Τίτλος Δουλειάς",job[0].text.strip())
print("Εταιρία:", span_tag.text)
#print(type(movie_containers))
#print(len(movie_containers))
#print(movie.splitlines())
#movie = movie.split()

apasxolisi = html_soup.find_all('div', class_="snapshot")
news_content = apasxolisi[0].find_all("div", {'class': 'snapshot-item'})
list=[]

for wrapper in apasxolisi[0].find_all("div", {'class': 'snapshot-item'}):
    list.append(wrapper.text)
    #print(wrapper.text)
print("Απασχοληση:",list[0].strip())
print("Περιοχή:",list[1].strip())


perigrafi = html_soup.find('div', class_="bloc")
news_content = perigrafi.find("h3", {'class': 'pb'})
news_content1 = perigrafi.find("div", {'class': ''})
print(news_content.text)
print(news_content1.text)