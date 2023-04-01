import requests
from bs4 import BeautifulSoup
import threading
import re
from abc import ABC, abstractmethod


class Scraper(ABC):

    @abstractmethod
    def start_scraping(self, link):
        pass

    @abstractmethod
    def insert_db(self, df, city):
        pass

    def __init__(self, link, city):
        self.link = link
        self.city = city
        self.ads = []
        self.lock = threading.Lock()
        self.threads = []

    def scrape(self):
        soup = self.get_soup(self.link)
        count_pages = self.get_page_count(soup)

        for i in range(count_pages):
            link = self.link if i == 0 else f"{self.link}?page={i + 1}"
            t = threading.Thread(target=self.start_scraping, args=(link,))
            self.threads.append(t)
            t.start()

        for thread in self.threads:
            thread.join()

        self.insert_db(self.ads, self.city)

    def get_soup(self, link):
        req = requests.get(link)
        return BeautifulSoup(req.text, 'lxml')

    def get_page_count(self, soup):
        return int(soup.select('li[data-testid="pagination-list-item"]')[3].text)

    def get_ad_links(self, soup):
        return [a['href'] for a in soup.select("a.css-rc5s2u")]

    def get_districts(self, soup):
        olx_districts = soup.find_all("p", attrs={"data-testid": "location-date"})
        districts = []
        for district in olx_districts:
            end = district.text.find(" -")
            districts.append(district.text[8:end])
        return districts

    def get_prices(self, soup):
        olx_buffer_prices = soup.find_all("p", attrs={"data-testid": "ad-price"})
        text_prices = ''.join(i.text.replace(' ', '').replace(',', '.') for i in olx_buffer_prices)
        olx_prices = [float(x) for x in re.findall(r'\d*\.\d+|\d+', text_prices)]
        return olx_prices
