import re


def room_type_scraping(soup):
    tags = soup.find_all('script')
    match = (r'"Liczba osób w pokoju","localizedValue":"(\D+)","currency"')
    if len(re.findall(match, tags[-1].text)) == 0:
        olx_room = 'unknown'
    else:
        olx_room = re.findall(match, tags[-1].text)[0].capitalize()
        if olx_room != 'Jednoosobowy' or olx_room != 'Dwuosobowy':
            olx_room = 'Trzyosobowy i więcej'

    return olx_room


"""
transakcja db
"""