from bs4 import BeautifulSoup

def getManufacurer(page: BeautifulSoup) -> str:
    manufacturer_name = page.find("span", itemprop="brand")
    if manufacturer_name:
        return manufacturer_name.get_text().strip()
    return ""