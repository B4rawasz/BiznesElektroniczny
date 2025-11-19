from bs4 import BeautifulSoup

import elements.name as element_name
import elements.category as element_category
<<<<<<< HEAD
import elements.price as element_price
import elements.manufacturer_img as element_manufacturer_img
=======
import elements.photos as element_photos
>>>>>>> 9229230edf72928d67e6dc55dfd1f9427d83303d

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
<<<<<<< HEAD
    result["price"] = element_price.getPrice(page)
    result["manufacturer_img"] = element_manufacturer_img.getManufacturerImg(page)
=======
    result["images"] = element_photos.getPhotos(page)
>>>>>>> 9229230edf72928d67e6dc55dfd1f9427d83303d

    return result