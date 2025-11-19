from bs4 import BeautifulSoup

def getManufacturerImg(page: BeautifulSoup) -> str:
    manufacturer_img = page.find("article", class_="product-page")
    if manufacturer_img and manufacturer_img.img:
        return manufacturer_img.img['src'].strip()
    return ""