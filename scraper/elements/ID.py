from bs4 import BeautifulSoup

def getID(page: BeautifulSoup) -> str:
    product_id = page.find("span", itemprop="productID")
    if product_id:
        return product_id.get("content").strip()
    return ""