import time
from helpers.helperOLX.apartment import tag_scraping, description_scraping
from helpers.helperOTODOM.apartment import area_scraping, room_type_scraping
from helpers.helperOTODOM.common import rent_scraping
from database.insertDB import add_new_apartment
from database.CompareFilters import compare_filters_new_apartment
from newScraper import NewScraper


class NewApartmentScraper(NewScraper):
    def __init__(self, city):
        self.previous_ad = ''
        self.city = city
        self.link = f'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{self.city}/'

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
                add_new_apartment(self.city, ad, olx_area, district, olx_rooms, price + olx_rent + bills, indicators)
                compare_filters_new_apartment()
                # email_sender(str(offer), sender, email_password, receiver)

            time.sleep(30)
