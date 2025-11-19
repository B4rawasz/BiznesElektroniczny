from bs4 import BeautifulSoup

import elements.name as element_name

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

    result["name"] = element_name.getName(page)

    return result