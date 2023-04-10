__author__ = 'Grzegorz Pustułka'
__version__ = "1.0.1"
__maintainer__ = "Grzegorz Pustułka"
__email__ = "kontakt.pustulka@gmail.com"
__status__ = "Development"

import threading
from Scraper.ApartmentScraper import ApartmentScraper
from Scraper.RoomScraper import RoomScraper
from database.createTable import create_room_table, create_apartment_table, create_apartment_filters_table, \
                                 create_users_table, create_new_apartment_table
from database.CompareFilters import compare_filters_new_apartment
from database.insertDB import add_user
from newScraper.NewApartmentScraper import NewApartmentScraper

if __name__ == '__main__':
    # create_room_table('wroclaw')
    # a = RoomScraper('wroclaw')
    # a.start()
    # create_apartment_table('krakow')
    # b = ApartmentScraper('krakow')
    # b.start()
    # create_room_table('krakow')
    # a = RoomScraper('krakow')
    # a.start()
    #
    # create_new_apartment_table()
    # a = NewApartmentScraper('krakow')
    # a.start()
    # check_filters_new_apartment = threading.Thread(target=compare_filters_new_apartment)
    # add_user('grzegorzpustulka@onet.pl')
