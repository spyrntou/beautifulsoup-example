#this is a simple crawler to crawl all links from page


import re
import requests
from bs4 import BeautifulSoup


# get all web site links
pages = set()

def get_links(page_url):
    global pages
    pattern = re.compile("^(/)")
    html = requests.get(f"https://www.example.gr/job_position?q=it").text  # fstrings require Python 3.6+
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", href=pattern):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")
