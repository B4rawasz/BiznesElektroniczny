from bs4 import BeautifulSoup

def getName(page: BeautifulSoup) -> str:
    category_nav = page.find("nav", class_="page-navigation")
    if category_nav:
        category_name = category_nav.find_all("a")[-1].get_text().strip()
        return category_name