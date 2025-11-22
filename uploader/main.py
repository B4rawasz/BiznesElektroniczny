import os
from pathlib import Path
import json
import re
import urllib3
import requests
from PIL import Image

import category_schema
import manufacturer_schema
import product_schema
import sale_schema
import stock_schema

TOTALY_SECRET_API_KEY = "2YNTE1A6YHCVRWAVT62V1GA58I7IMI5Q"
BASE_URL = "https://localhost/api/"

BASE_PATH = Path(__file__).resolve().parent.resolve()
SCRAPER_PATH = BASE_PATH.parent.resolve() / "scraper"
CATEGORY_TREE_PATH = SCRAPER_PATH / "item_categories.json"
MANUFACTURERS_PATH = SCRAPER_PATH / "manufacturers.json"
DATA_PATH = SCRAPER_PATH / "resoult"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sanitize_folder_name(name):
    """Remove or replace invalid characters for Windows folder names"""
    # Replace invalid characters with underscore
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, '_', name)
    # Remove trailing dots and spaces
    sanitized = sanitized.rstrip('. ')
    return sanitized

category_tree = {}
with open(CATEGORY_TREE_PATH, "r", encoding="utf-8") as f:
        category_tree = json.load(f)

manufacturers_tree = {}
with open(MANUFACTURERS_PATH, "r", encoding="utf-8") as f:
        manufacturers_tree = json.load(f)

manufacturers_ids = {}
category_ids = {}

def upload_manufacturers():
    for manufacturer, logo_path in manufacturers_tree.items(): 
        xml_data = manufacturer_schema.toXAMLManufacturerSchema(
            name=manufacturer
        )

        response = requests.post(
            BASE_URL + "manufacturers",
            data=xml_data,
            auth=(TOTALY_SECRET_API_KEY, ''),
            headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
            verify=False
        )

        if response.status_code == 201:
            response_data = response.json()
            new_manufacturer_id = response_data['manufacturer']['id']
            manufacturers_ids[manufacturer] = new_manufacturer_id
            print(f"Uploaded manufacturer '{manufacturer}' with ID {new_manufacturer_id}")

            with open(logo_path, "rb") as img_file:
                files = {'image': img_file}
                img_response = requests.post(
                    BASE_URL + f"images/manufacturers/{new_manufacturer_id}",
                    auth=(TOTALY_SECRET_API_KEY, ''),
                    files=files,
                    verify=False
                )
                if img_response.status_code == 200:
                    print(f"Uploaded logo for manufacturer '{manufacturer}'")
                else:
                    print(f"Failed to upload logo for '{manufacturer}': {img_response.status_code} - {img_response.text}")
        else:
            print(f"Failed to upload manufacturer '{manufacturer}': {response.text}")

def upload_category(parent_id: int, category_name: str, subcategories: dict):
    
    sanitized_category_name = sanitize_folder_name(category_name)
    category_path = DATA_PATH / "categories" / sanitized_category_name
    data_file_path = category_path / "data.json"

    image_path = DATA_PATH / "categories" / "images" / f"{sanitized_category_name}.webp"

    description = ""

    if data_file_path.exists():
        with open(data_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            description = data.get("description")

    xml_data = category_schema.toXAMLCategorySchema(
        category=category_name,
        description=description,
        id_parent=parent_id
    )

    response = requests.post(
        BASE_URL + "categories",
        data=xml_data,
        auth=(TOTALY_SECRET_API_KEY, ''),
        headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
        verify=False
    )

    if response.status_code == 201:
        response_data = response.json()
        new_category_id = response_data['category']['id']
        category_ids[category_name] = new_category_id
        print(f"Uploaded category '{category_name}' with ID {new_category_id}")

        if image_path.exists():
            with Image.open(image_path) as img:
                img.save("temp_image.png", "png")

            with open("temp_image.png", "rb") as img_file:
                files = {'image': img_file}
                img_response = requests.post(
                    BASE_URL + f"images/categories/{new_category_id}",
                    auth=(TOTALY_SECRET_API_KEY, ''),
                    files=files,
                    verify=False
                )
                if img_response.status_code == 200:
                    print(f"Uploaded image for category '{category_name}'")
                else:
                    print(f"Failed to upload image for '{category_name}': {img_response.status_code} - {img_response.text}")

        for subcat_name, subcat_children in subcategories.items():
            upload_category(new_category_id, subcat_name, subcat_children)
    else:
        print(f"Failed to upload category '{category_name}': {response.text}")

def upload_products():
    for dirpath, _, filenames in os.walk(DATA_PATH / "Hard-PC.pl"):
        for fn in filenames:
            if fn.lower() != "data.json":
                continue
            fp = Path(dirpath) / fn
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                continue

            manufacturer_name = data.get("manufacturer")
            manufacturer_id = manufacturers_ids.get(manufacturer_name)

            if manufacturer_id is None:
                print(f"Manufacturer '{manufacturer_name}' not found for product '{data.get('name', '')}'. Skipping product.")
                continue

            category_name = data.get("category")[-1]
            category_id = category_ids.get(category_name, 2)

            product_data = product_schema.toXAMLProductSchema(
                manufacturer_id=manufacturer_id,
                price=data.get("price", 0.0),
                name=data.get("name", ""),
                description=data.get("description", ""),
                short_description=data.get("security_data", ""),
                category_id=category_id,
                code=data.get("code", "")
            )

            response = requests.post(
                BASE_URL + "products",
                data=product_data['xml'],
                auth=(TOTALY_SECRET_API_KEY, ''),
                headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
                verify=False
            )

            if product_data['on_sale']:
                json_data = response.json()
                xaml_sale_data = sale_schema.toXAMLSaleSchema(
                    product_id=int(json_data['product']['id'])
                )
                sale_response = requests.post(
                    BASE_URL + "specific_prices",
                    data=xaml_sale_data,
                    auth=(TOTALY_SECRET_API_KEY, ''),
                    headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
                    verify=False
                )

            if response.status_code == 201:
                response_data = response.json()
                new_product_id = response_data['product']['id']

                stock_response = requests.get(
                    BASE_URL + f"stock_availables?filter[id_product]={new_product_id}&display=full",
                    auth=(TOTALY_SECRET_API_KEY, ''),
                    headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
                    verify=False
                )

                stock_response_data = stock_response.json()
                stock_response_data_id = stock_response_data['stock_availables'][0]['id']

                stock_xml = stock_schema.toXAMLStockSchema(
                    product_id=new_product_id,
                    id=stock_response_data_id
                )

                stock_update_response = requests.put(
                    BASE_URL + f"stock_availables/{stock_response_data_id}",
                    data=stock_xml,
                    auth=(TOTALY_SECRET_API_KEY, ''),
                    headers={'Content-Type': 'application/xml', 'Output-Format': 'JSON'},
                    verify=False
                )

                # upload images
                for img_idx in range(1, 4):
                    image_path = Path(dirpath) / f"image_{img_idx}.webp"
                    if not image_path.exists():
                        continue

                    with Image.open(image_path) as img:
                        img.save("temp_image.png", "png")

                    # check if image is under 2MB, if not, resize
                    if os.path.getsize("temp_image.png") > 2 * 1024 * 1024:
                        with Image.open("temp_image.png") as img:
                            # save proportions
                            aspect_ratio = img.width / img.height
                            new_width = 1024
                            new_height = int(new_width / aspect_ratio)
                            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                            img.save("temp_image.png", "png")

                    with open("temp_image.png", "rb") as img_file:
                        files = {'image': img_file}
                        img_response = requests.post(
                            BASE_URL + f"images/products/{new_product_id}",
                            auth=(TOTALY_SECRET_API_KEY, ''),
                            files=files,
                            verify=False
                        )
                        if img_response.status_code == 200:
                            print(f"Uploaded image {img_idx} for product '{data.get('name', '')}'")
                        else:
                            print(f"Failed to upload image {img_idx} for '{data.get('name', '')}': {img_response.status_code} - {img_response.text}")

                print(f"Uploaded product '{data.get('name', '')}' with ID {new_product_id}")
            else:
                print(f"Failed to upload product '{data.get('name', '')}': {response.text}")


upload_manufacturers()
for category_name, subcategories in category_tree['Hard-PC.pl'].items():
    upload_category(parent_id=2, category_name=category_name, subcategories=subcategories)

upload_products()