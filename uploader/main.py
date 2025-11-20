from pathlib import Path
import json
import re

import requests

import category_schema

TOTALY_SECRET_API_KEY = "VBEMRGR6HNXK1TVBVF7YBIAM157WTMN4"
BASE_URL = "https://localhost/api/"

BASE_PATH = Path(__file__).resolve().parent.resolve()
SCRAPER_PATH = BASE_PATH.parent.resolve() / "scraper"
CATEGORY_TREE_PATH = SCRAPER_PATH / "item_categories.json"
DATA_PATH = SCRAPER_PATH / "resoult"

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
        print(f"Uploaded category '{category_name}' with ID {new_category_id}")

        for subcat_name, subcat_children in subcategories.items():
            upload_category(new_category_id, subcat_name, subcat_children)
    else:
        print(f"Failed to upload category '{category_name}': {response.text}")

for category_name, subcategories in category_tree['Hard-PC.pl'].items():
    upload_category(parent_id=2, category_name=category_name, subcategories=subcategories)