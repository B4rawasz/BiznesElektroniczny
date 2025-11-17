from bs4 import BeautifulSoup

def extract(page: BeautifulSoup) -> dict:
    result = {
        "category": [],
        "name": "",
        "price": 0,
        "description": "",
        "technical_data": "",
        "security_data": "",
        "manufacturer_img": "",
        "images": []
        }

    breadcrumb = page.find("div", class_="breadcrumb")
    if breadcrumb:
        for crumb in breadcrumb.find_all("a"):
            result["category"].append(crumb.get_text().strip())

    product_name = page.find("h1", class_="product-title")
    if product_name:
        result["name"] = product_name.get_text().strip()

    return result