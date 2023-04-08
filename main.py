__author__ = 'Grzegorz Pustułka'
__version__ = "1.0.1"
__maintainer__ = "Grzegorz Pustułka"
__email__ = "kontakt.pustulka@gmail.com"
__status__ = "Development"

from Scraper.ApartmentScraper import ApartmentScraper
from Scraper.RoomScraper import RoomScraper
from database.createTable import create_room_table, create_apartment_table

if __name__ == '__main__':
    # create_room_table('wroclaw')
    # a = RoomScraper('wroclaw')
    # a.start()
    # create_apartment_table('krakow')
    b = ApartmentScraper('krakow')
    b.start()

    # create_room_table('krakow')
    # a = RoomScraper('krakow')
    # a.start()
