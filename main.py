__author__ = 'Grzegorz Pustułka'
__version__ = "1.0.1"
__maintainer__ = "Grzegorz Pustułka"
__email__ = "kontakt.pustulka@gmail.com"
__status__ = "Development"

from Scraper.ApartmentScraper import ApartmentScraper
from Scraper.RoomScraper import RoomScraper
from database.createTable import create_room_table, create_apartment_table


if __name__ == '__main__':
    create_room_table('lodz')
    a = RoomScraper('lodz')
    a.start()

    create_apartment_table('lodz')
    b = ApartmentScraper('lodz')
    b.start()



