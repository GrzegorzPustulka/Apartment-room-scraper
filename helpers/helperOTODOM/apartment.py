import re


def area_scraping(soup):
    tags = soup.find_all('script')
    match = (r'"key":"m","value":"(\d+.?\d+)"')

    if len(re.findall(match, tags[-1].text)) == 0:
        olx_area = 'unknown'
    else:
        olx_area = re.findall(match, tags[-1].text)[0]

    return olx_area.replace(",", ".")


def room_type_scraping(soup):
    tags = soup.find_all('script')
    match = (r'"key":"rooms_num","value":"(\d+)"')
    if len(re.findall(match, tags[-1].text)) == 0:
        olx_rooms = 'unknown'
    else:
        olx_rooms = int(re.findall(match, tags[-1].text)[0])
        if olx_rooms == 1:
            olx_rooms = 'Kawalerka'
        elif olx_rooms == 2:
            olx_rooms = '2 pokoje'
        elif olx_rooms == 3:
            olx_rooms = '3 pokoje'
        else:
            olx_rooms = '4 i więcej'

    return olx_rooms
