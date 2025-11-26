import json
import random
import re
import time
from bs4 import BeautifulSoup
import requests
from pathlib import Path

import extractor

base_url = "https://sklep.hard-pc.pl"
site_map = "/sitemap.php"
pduct_key = "/p"
category_key = "/k"

BASE_PATH = Path(__file__).resolve().parent.resolve()
DATA_PATH = BASE_PATH / "resoult"

DATA_PATH.mkdir(exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def sanitize_folder_name(name):
    """Remove or replace invalid characters for Windows folder names"""
    # Replace invalid characters with underscore
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, '_', name)
    # Remove trailing dots and spaces
    sanitized = sanitized.rstrip('. ')
    return sanitized

response = requests.get(base_url + site_map, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

product_links = []
category_links = []
for link in soup.find_all("a", href=True):
    if base_url + pduct_key in link['href']:
        product_links.append(link['href'])
    elif base_url + category_key in link['href']:
        category_links.append(link['href'])

with open("product_links.txt", "w", encoding="utf-8") as file:
    for product_link in product_links:
        file.write(product_link + "\n")

with open("category_links.txt", "w", encoding="utf-8") as file:
    for category_link in category_links:
        file.write(category_link + "\n")

def scrape_products():
    for idx, product_link in enumerate(product_links):
        delay = random.uniform(2, 4)
        time.sleep(delay)

        print(f"Processing product {idx + 1}/{len(product_links)}: {product_link}")
        response_product = requests.get(product_link, headers=headers)
        soup_product = BeautifulSoup(response_product.content, "html.parser")
        data = extractor.extract(soup_product)

        #from data[category] list make folder structure
        category_path = DATA_PATH
        for category in data['category']:
            sanitized_category = sanitize_folder_name(category)
            category_path = category_path / sanitized_category
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

def scrape_categories():
    category_path = DATA_PATH / "categories"
    category_path.mkdir(exist_ok=True)
    category_img_path = category_path / "images"
    category_img_path.mkdir(exist_ok=True)

    for idx, category_link in enumerate(category_links):
        delay = random.uniform(2, 4)
        time.sleep(delay)

        print(f"Processing category {idx + 1}/{len(category_links)}: {category_link}")
        response_category = requests.get(category_link, headers=headers)
        soup_category = BeautifulSoup(response_category.content, "html.parser")

        data = extractor.extract_category(soup_category)

        category_name = sanitize_folder_name(data["name"])
        file_path = category_path / category_name
        file_path.mkdir(exist_ok=True)

        with open(file_path / "data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        for idx, sub_image in enumerate(data["sub_images"]):
            image_url = sub_image["image_url"]
            image_response = requests.get(base_url + "/" + image_url, headers=headers)
            image_extension = image_url.split(".")[-1]
            sanitized_subcategory_name = sanitize_folder_name(sub_image["name"])
            with open(category_img_path / f"{sanitized_subcategory_name}.{image_extension}", "wb") as img_file:
                img_file.write(image_response.content)        

    print("Category scraping completed.")

#scrape_products()
scrape_categories()