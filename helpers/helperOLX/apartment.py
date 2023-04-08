import re


def tag_scraping(soup):
    olx_rent = 0
    olx_area = 'unknown'
    olx_rooms = 'unknown'
    tags = soup.select('li.css-1r0si1e')
    for tag in tags:
        if "Czynsz" in tag.text:
            text_prices = tag.text.replace(' ', '').replace(',', '.')
            olx_rent = (int(re.findall(r'\d+', text_prices)[0]))
        elif "Powierzchnia" in tag.text:
            olx_area = tag.text[14:-3]
        elif "Liczba pokoi: " in tag.text:
            olx_rooms = tag.text[14:]
    return olx_rent, olx_area.replace(",", "."), olx_rooms


def description_scraping(soup, rent):
    additional_fees = 0
    try:
        description = soup.select('.css-bgzo2k.er34gjf0')[0].text
    except IndexError:
        return -1
    description = description.lower()
    sentences = re.split(r'[.\n+]', description)
    description_to_re = ''
    unwanted_words = ['kaucj', 'opcjonaln', 'gara', 'parkin', 'osoby', 'osobach']
    flag = True
    for sentence in sentences:
        for unwanted_word in unwanted_words:
            if unwanted_word in sentence:
                flag = False
                break
        if flag:
            description_to_re += sentence
        flag = True

    mo = r"(\d+\s?,?\d+(zł|zl| zł| zl|pln| pln|złoty| zloty| \(|\())"
    bills = re.findall(mo, description_to_re)
    bills = ["".join(x) for x in bills]

    for j in range(len(bills)):
        bills[j] = ''.join(x for x in bills[j] if x.isdigit())
    bills[:] = list(set(bills))
    bills[:] = [float(x) for x in list(set(bills)) if float(x) < 700]
    for bill in bills:
        if float(bill) == rent:
            continue
        else:
            additional_fees += bill

    indicators_words = ['licznik', 'wedlug', 'wg', 'zużyci', 'zuzyci', 'według', "+ media"]
    indicators = False
    for indicator in indicators_words:
        if indicator in description:
            indicators = True
            break
    return [additional_fees, indicators]
