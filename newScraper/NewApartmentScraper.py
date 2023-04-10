import requests
from bs4 import BeautifulSoup
import time
import re
from helpers.helperOLX.apartment import tag_scraping, description_scraping
from helpers.helperOTODOM.apartment import area_scraping, room_type_scraping
from helpers.helperOTODOM.common import rent_scraping
from dataClasses.dataClass import AdsNewApartment
from database.insertDB import add_new_apartment


class NewApartmentScraper:
    def __init__(self, city):
        self.city = city
        self.link = f'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{self.city}/'
        self.ads = []
        self.previous_ad = ''

    def start(self):
        while True:
            soup = self.get_soup(self.link)

            # link
            ad = soup.select("a.css-rc5s2u")[3]['href']
            ad = self.fix_link(ad)

            district = self.get_district(soup)
            price = self.get_price(soup)

            soup = self.get_soup(ad)
            if "olx.pl" in ad:
                olx_rent, olx_area, olx_rooms = tag_scraping(soup)
                bills, indicators = description_scraping(soup, olx_rent)
            else:
                olx_rent = rent_scraping(soup)
                olx_area = area_scraping(soup)
                olx_rooms = room_type_scraping(soup)
                bills = 0
                indicators = False

            if ad != self.previous_ad:
                self.previous_ad = ad
                add_new_apartment(self.city, ad, olx_area, district, olx_rooms, price, olx_rent, bills, price + olx_rent + bills, indicators)
                # email_sender(str(offer), sender, email_password, receiver)

            time.sleep(30)

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

