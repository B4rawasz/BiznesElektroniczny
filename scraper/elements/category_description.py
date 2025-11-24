from bs4 import BeautifulSoup

def getDescription(page: BeautifulSoup) -> str:
    article = page.find("article", class_="module-about")
    if article:
        desc = article.find("header")
        html_parts = []
        for element in desc.children:
            if hasattr(element, 'name'):
                html_parts.append(str(element))
        
        description = ''.join(html_parts)

        return description.replace('\n', '').strip()
    return ""