def image_scraping(soup):
    images = []
    containers = soup.select('.swiper-zoom-container')
    for container in containers:
        for img in container.find_all('img'):
            src = img.get('src')
            if src is not None:
                images.append(src)
    return images
