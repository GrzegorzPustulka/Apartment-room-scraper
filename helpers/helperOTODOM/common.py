import re


def rent_scraping(soup):
    tags = soup.find_all('script')
    match = (r'"key":"rent","value":"(\d+)"')

    if len(re.findall(match, tags[-1].text)) == 0:
        rent = 0
    else:
        rent = int(re.findall(match, tags[-1].text)[0])

    return rent
