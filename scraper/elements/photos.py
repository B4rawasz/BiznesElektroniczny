from bs4 import BeautifulSoup

def getPhotos(page: BeautifulSoup) -> list:
    photos = []
    image_gallery = page.find("div", class_="module-gallery")
    if image_gallery:
        for img_tag in image_gallery.find_all("img"):
            img_url = img_tag.get("src")
            if img_url:
                img_url = img_url.replace("_p.", ".") # pobierał pełnowymiarowe zdjęcia
                photos.append(img_url)
    return photos