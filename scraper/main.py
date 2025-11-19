import json
import random
import time
from bs4 import BeautifulSoup
import requests
from pathlib import Path

import extractor

base_url = "https://sklep.hard-pc.pl"
site_map = "/sitemap.php"
pduct_key = "/p"

BASE_PATH = Path(__file__).resolve().parent.resolve()
DATA_PATH = BASE_PATH / "resoult"

DATA_PATH.mkdir(exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(base_url + site_map, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

product_links = []
for link in soup.find_all("a", href=True):
    if base_url + pduct_key in link['href']:
        product_links.append(link['href'])

with open("product_links.txt", "w", encoding="utf-8") as file:
    for product_link in product_links:
        file.write(product_link + "\n")

#response_product = requests.get(product_links[0])
#soup_product = BeautifulSoup(response_product.content, "html.parser")

#with open("sample_product.html", "w", encoding="utf-8") as file:
#    file.write(str(soup_product))

#data = extractor.extract(soup_product)

for idx, product_link in enumerate(product_links[:1800]):
    delay = random.uniform(2, 4)
    time.sleep(delay)

    print(f"Processing product {idx + 1}/{len(product_links[:1800])}: {product_link}")

    response_product = requests.get(product_link, headers=headers)
    soup_product = BeautifulSoup(response_product.content, "html.parser")
    data = extractor.extract(soup_product)

    #from data[category] list make folder structure
    category_path = DATA_PATH
    for category in data['category']:
        category_path = category_path / category
        category_path.mkdir(exist_ok=True)
    file_path = category_path / data["id"]
    file_path.mkdir(exist_ok=True)

    with open(file_path / "data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # Download images
    for idx, image_url in enumerate(data["images"]):
        if idx == 3:
            break
        image_response = requests.get(base_url + "/" + image_url, headers=headers)
        image_extension = image_url.split(".")[-1]
        with open(file_path / f"image_{idx + 1}.{image_extension}", "wb") as img_file:
            img_file.write(image_response.content)

    # Download manufacturer logo
    manufacturer_logo = data["manufacturer_img"]
    if manufacturer_logo:
        logo_response = requests.get(base_url + "/" + manufacturer_logo, headers=headers)
        logo_extension = manufacturer_logo.split(".")[-1]
        with open(file_path / f"manufacturer_logo.{logo_extension}", "wb") as logo_file:
            logo_file.write(logo_response.content)

print("Scraping completed.")