from bs4 import BeautifulSoup

import elements.name as element_name
import elements.category as element_category
import elements.price as element_price
import elements.description as element_description
import elements.manufacturer_img as element_manufacturer_img
import elements.photos as element_photos

def extract(page: BeautifulSoup) -> dict:
    result = {
        "category": [],
        "name": "",
        "price": 0,
        "description": "",
        "security_data": "",
        "manufacturer_img": "",
        "images": []
        }

    result["category"] = element_category.getCategory(page)
    result["name"] = element_name.getName(page)
    result["price"] = element_price.getPrice(page)
    result["description"] = element_description.getDescription(page)
    result["manufacturer_img"] = element_manufacturer_img.getManufacturerImg(page)
    result["images"] = element_photos.getPhotos(page)

    return result