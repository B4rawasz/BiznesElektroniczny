from bs4 import BeautifulSoup

def getName(page: BeautifulSoup) -> str:
    product_name = page.find("h1", itemprop="name")
    if product_name:
        return product_name.get_text().strip()
    return ""