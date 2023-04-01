from helpers.helperCommon.common import olx_or_otodom
from helpers.helperOLX.room import description_scraping, tag_scraping
from helpers.helperOLX.common import image_scraping
from helpers.helperOTODOM.common import rent_scraping
from helpers.helperOTODOM.room import room_type_scraping
from Scraper.Scraper import Scraper
from dataClasses.dataClass import AdsRoom
from database.insertDB import insert_rooms_db
import requests


class RoomScraper(Scraper):
    def __init__(self, city):
        self.city = city
        self.link = f'https://www.olx.pl/d/nieruchomosci/stancje-pokoje/{self.city}/'
        super().__init__(self.link, self.city)

    def start(self):
        super().scrape()

    def start_scraping(self, link):
        soup = self.get_soup(link)
        ad = soup.select("a.css-rc5s2u")
        olx_ad = olx_or_otodom(ad)
        districts = self.get_districts(soup)
        olx_prices = self.get_prices(soup)

        for i, link in enumerate(olx_ad):
            soup = self.get_soup(link)

            if "olx.pl" in link:
                image = image_scraping(soup)
                additional_fees = description_scraping(soup)
                if additional_fees == -1:
                    break
                type_room = tag_scraping(soup)
            else:
                additional_fees = rent_scraping(soup)
                type_room = room_type_scraping(soup)
                image = ''
            ad = AdsRoom(olx_ad[i], districts[i], type_room, olx_prices[i], additional_fees,
                         olx_prices[i] + additional_fees, image)
            with self.lock:
                self.ads.append(ad)

    def insert_db(self, ads, city):
        insert_rooms_db(ads, city)


