import re


def rent_scraping(soup):
    tags = soup.find_all('script')
    match = (r'"key":"rent","value":"(\d+)"')

    if len(re.findall(match, tags[-1].text)) == 0:
        rent = 0
    else:
        rent = int(re.findall(match, tags[-1].text)[0])

    return rent


def image_scraping_otodom(soup):
    tags = soup.find_all('script')
    pattern = r'https://ireland.apollo.*?"'
    matches = re.findall(pattern, tags[-1].text)
    imagines = []
    for i in range(len(matches) - 1):
        # are the same url, the difference is only in size
        if matches[i][0:90] != matches[i + 1][0:90]:
            imagines.append(matches[i])
    return imagines
