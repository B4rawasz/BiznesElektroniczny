from bs4 import BeautifulSoup

import elements.name as element_name
import elements.category as element_category
import elements.price as element_price
import elements.manufacturer_img as element_manufacturer_img

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

    result["category"] = element_category.getCategory(page)
    result["name"] = element_name.getName(page)
    result["price"] = element_price.getPrice(page)
    result["manufacturer_img"] = element_manufacturer_img.getManufacturerImg(page)

    return result