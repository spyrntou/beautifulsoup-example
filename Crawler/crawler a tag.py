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
import scrapy




print("------------------------ Script just started ------------------------")

class QuotesSpider(scrapy.Spider):
    name = 'kariera'
    start_urls = [
        'https://www.kariera.gr/θέσεις-εργασίας',
    ]

    def parse(self, response):
        for quote in response.css('div.job'):
            yield {
                'job-title': quote.css('div.text::text').get()
                    }
            return quote
