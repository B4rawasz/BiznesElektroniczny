from bs4 import BeautifulSoup

def getPrice(page: BeautifulSoup) -> float:
    product_price = page.find("div", class_="prices")
    if product_price:
        return float(product_price.get_attribute_list("rawprice")[0].strip())

    return 0.0