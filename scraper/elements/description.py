from bs4 import BeautifulSoup

def getDescription(page: BeautifulSoup) -> str:
    desctription_section = page.find('article', id='section-descriptions')

    description_div = desctription_section.find("div", class_="inner", itemprop="description")
    if not description_div:
        return ""
    
    article = description_div.find("section", class_="no-mobile")
    
    if article:
        html_parts = []
        for element in description_div.children:
            if element == article:
                break
            if hasattr(element, 'name'):
                html_parts.append(str(element))
        
        description = ''.join(html_parts)

        return description.replace('\n', '').strip()
    else:
        return description_div.decode_contents().replace('\n', '').strip()