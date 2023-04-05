from helpers.helperCommon.common import olx_or_otodom
from helpers.helperOLX.apartment import tag_scraping, description_scraping
from helpers.helperOLX.common import image_scraping
from helpers.helperOTODOM.apartment import area_scraping, room_type_scraping
from helpers.helperOTODOM.common import rent_scraping
from Scraper.Scraper import Scraper
from dataClasses.dataClass import AdsApartment
from database.insertDB import insert_apartments_db
from helpers.helperOTODOM.common import image_scraping_otodom


class ApartmentScraper(Scraper):
    def __init__(self, city):
        self.city = city
        self.link = f'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{self.city}/'
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
                olx_rent, olx_area, olx_rooms, = tag_scraping(soup)
                images = image_scraping(soup)
                bills = description_scraping(soup, olx_rent)
                source = 'olx'
            else:
                olx_rent = rent_scraping(soup)
                olx_area = area_scraping(soup)
                olx_rooms = room_type_scraping(soup)
                images = image_scraping_otodom(soup)
                bills = 0
                source = 'otodom'
            ad = AdsApartment(olx_ad[i], source, olx_area, districts[i], olx_rooms, olx_prices[i], olx_rent, bills,
                              olx_prices[i] + olx_rent + bills, images)
            with self.lock:
                self.ads.append(ad)

    def insert_db(self, ads, city):
        insert_apartments_db(ads, city)
