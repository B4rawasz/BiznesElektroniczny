from bs4 import BeautifulSoup
import requests

import extractor

base_url = "https://sklep.hard-pc.pl"
site_map = "/sitemap.php"
pduct_key = "/p"

response = requests.get(base_url + site_map)
soup = BeautifulSoup(response.content, "html.parser")

product_links = []
for link in soup.find_all("a", href=True):
    if base_url + pduct_key in link['href']:
        product_links.append(link['href'])

with open("product_links.txt", "w", encoding="utf-8") as file:
    for product_link in product_links:
        file.write(product_link + "\n")

response_product = requests.get(product_links[0])
soup_product = BeautifulSoup(response_product.content, "html.parser")

with open("sample_product.html", "w", encoding="utf-8") as file:
    file.write(str(soup_product))

data = extractor.extract(soup_product)

print(data)
