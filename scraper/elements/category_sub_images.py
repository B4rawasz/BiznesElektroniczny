from bs4 import BeautifulSoup

def getSubCeategoryImages(page: BeautifulSoup) -> list:
    images = []
    subcategory_list = page.find("div", class_="list-categories")
    if subcategory_list:
        for subcategory in subcategory_list.children:
            subcategory_name = subcategory.find("a").text.strip()
            subcategory_img_tag = subcategory.find("figure").find("img")
            if subcategory_img_tag and 'src' in subcategory_img_tag.attrs:
                subcategory_img_url = subcategory_img_tag['src']
                images.append({
                    "name": subcategory_name,
                    "image_url": subcategory_img_url
                })
        return images

    return []