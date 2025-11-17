from bs4 import BeautifulSoup
import requests

base_url = "https://sklep.hard-pc.pl"
site_map = "/sitemap.php"
pduct_key = "/p"

response = requests.get(base_url + site_map)
soup = BeautifulSoup(response.content, "html.parser")

product_links = []
for link in soup.find_all("a", href=True):
    if base_url + pduct_key in link['href']:
        product_links.append(link['href'])
