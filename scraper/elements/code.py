from bs4 import BeautifulSoup

def getCode(page: BeautifulSoup) -> str:
    code_element = page.find("meta", itemprop="sku")
    if code_element:
        return code_element.get("content").strip()
    return ""   