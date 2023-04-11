import NewScraper
import time
from helpers.helperOLX.room import description_scraping, tag_scraping
from helpers.helperOTODOM.room import room_type_scraping
from helpers.helperOTODOM.common import rent_scraping
from database.CompareFilters import compare_filters_new_room
class NewRoomScraper(NewScraper):
    def __init__(self, city):
        self.previous_ad = ''
        self.city = city
        self.link = f'https://www.olx.pl/d/nieruchomosci/stancje-pokoje/{self.city}/'

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
                additional_fees = description_scraping(soup)
                if additional_fees == -1:
                    continue
                room_type = tag_scraping(soup)
            else:
                additional_fees = rent_scraping(soup)
                room_type = room_type_scraping(soup)

            if ad != self.previous_ad:
                self.previous_ad = ad
                compare_filters_new_room(self.city, ad, district, room_type, price, additional_fees)
                # email_sender(str(offer), sender, email_password, receiver)

            time.sleep(30)
