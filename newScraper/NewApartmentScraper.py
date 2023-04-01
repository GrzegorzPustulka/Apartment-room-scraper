# import requests
# from bs4 import BeautifulSoup
# import time
#
# from helpers.helperOLX.apartment import tag_scraping, description_scraping
# from helpers.helperOTODOM.apartment import area_scraping, room_type_scraping
# from helpers.helperOTODOM.common import rent_scraping
# from dataClasses.dataClass import AdsNewApartment
#
#
# class NewApartmentScraper:
#     def __init__(self, city):
#         self.city = city
#         self.link = f'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{self.city}/'
#         self.ads = []
#         self.previous_ad = ''
#
#     def start(self):
#         while True:
#             req = requests.get(self.link)
#             soup = BeautifulSoup(req.text, 'lxml')
#
#             # link
#             ad = soup.select("a.css-rc5s2u")[3]['href']
#             if "otodom" not in ad:
#                 ad = "https://www.olx.pl" + ad
#
#             # district
#             district = soup.find_all("p", attrs={"data-testid": "location-date"})[3].text
#             end_index = district.find(" -")
#             district = district[8:end_index]
#
#             price = soup.find_all("p", attrs={"data-testid": "ad-price"})[3].text.replace(' ', '').replace(',', '.').replace(',', '.').replace('zł', '')
#             price = float(price)
#
#             soup = BeautifulSoup(req.text, 'lxml')
#             if "olx.pl" in ad:
#                 olx_rent, olx_area, olx_rooms = tag_scraping(soup)
#             else:
#                 olx_rent = rent_scraping(soup)
#                 olx_area = area_scraping(soup)
#                 olx_rooms = room_type_scraping(soup)
#
#             if ad != self.previous_ad:
#                 self.previous_ad = ad
#                 offer = AdsNewApartment(ad, olx_area, district, olx_rooms, price, olx_rent, price + olx_rent)
#                 self.ads.append(offer)
#                 # email_sender(str(offer), sender, email_password, receiver)
#
#             time.sleep(30)
#
#     def get_soup(self, link):
#         req = requests.get(link)
#         return BeautifulSoup(req.text, 'lxml')
#
