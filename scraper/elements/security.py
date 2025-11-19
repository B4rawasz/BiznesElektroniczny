from bs4 import BeautifulSoup

def getSecurityData(page: BeautifulSoup) -> str:
    security_section = page.find('div', class_='wizytowka')
    if not security_section:
        return ""
    
    for email_elem in security_section.find_all('a', class_='__cf_email__'):
        encoded = email_elem.get('data-cfemail')
        if encoded:
            decoded_email = decode_cloudflare_email(encoded)
            email_elem.replace_with(decoded_email)
    
    return security_section.decode_contents().replace('\n', '').strip()

def decode_cloudflare_email(encoded_string):
    r = int(encoded_string[:2], 16)
    email = ''.join([chr(int(encoded_string[i:i+2], 16) ^ r) for i in range(2, len(encoded_string), 2)])
    return email