from bs4 import BeautifulSoup

import elements.name as element_name
import elements.category as element_category
import elements.photos as element_photos

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
    result["images"] = element_photos.getPhotos(page)

    return result