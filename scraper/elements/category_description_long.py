from bs4 import BeautifulSoup

def getDescription(page: BeautifulSoup) -> str:
    article = page.find("article", class_="module-a")
    if article:
        html_parts = []
        for element in article.children:
            if hasattr(element, 'name'):
                html_parts.append(str(element))
        
        description = ''.join(html_parts)

        return description.replace('\n', '').strip()
    return ""