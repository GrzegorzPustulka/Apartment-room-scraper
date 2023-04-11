import re
import requests
from bs4 import BeautifulSoup


class NewScraper:

    def get_soup(self, link):
        req = requests.get(link)
        return BeautifulSoup(req.text, 'lxml')

    def get_district(self, soup):
        district_id = soup.find_all("p", attrs={"data-testid": "location-date"})[3]
        start = district_id.text.find(", ")
        end = district_id.text.find(" -")
        district = (district_id.text[start+2:end])
        return district

    def get_price(self, soup):
        olx_buffer_price = soup.find_all("p", attrs={"data-testid": "ad-price"})[3]
        text_price = ''.join(i.text.replace(' ', '').replace(',', '.') for i in olx_buffer_price)
        olx_price = [float(x) for x in re.findall(r'\d*\.\d+|\d+', text_price)]
        return olx_price[0]

    def fix_link(self, link):
        if 'otodom' in link:
            return link
        elif 'olx' not in link:
            link = "https://www.olx.pl" + link

        if link[-1] == '?':
            return link[:-1]
        else:
            return link
