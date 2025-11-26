from bs4 import BeautifulSoup

def getCategory(page: BeautifulSoup) -> list:
    categories = []
    category_nav = page.find("nav", class_="page-navigation")
    if category_nav:
        for link in category_nav.find_all("a"):
            category_name = link.get_text().strip()
            if category_name:
                categories.append(category_name)
    return categories