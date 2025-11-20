import re
from bs4 import BeautifulSoup
import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.resolve().parent
DATA_PATH = BASE_PATH / "resoult" / "Hard-PC.pl"

def getManufacurer(page: BeautifulSoup) -> str:
    manufacturer_name = page.find("span", itemprop="brand")
    if manufacturer_name:
        return manufacturer_name.get_text().strip()
    return ""

def getManufacturerFromSecurityData(html):
    if not html:
        return None
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True)
    match = re.search(r'Producent\b\s*[:\-–]?\s*(.+?)\s+Dane producenta\b', text, flags=re.I | re.S)
    print(match)
    if match:
        return match.group(1).strip()
    return None

def updateFile(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        print("Failed to read JSON from:", path)
        return False
    
    if data.get("manufacturer"):
        return False  # already has manufacturer
    
    manufacturer = getManufacturerFromSecurityData(data.get("security_data"))

    if manufacturer:
        print(f"Found manufacturer '{manufacturer}' in security data for: {path}")
    else:
        cat = data.get("category", [])
        if cat[1] == 'Komputery Hard-Pc':
            manufacturer = 'Hard-PC'

    if manufacturer:
        data["manufacturer"] = manufacturer
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Updated manufacturer in:", path)
            return True
        except Exception:
            print("Failed to write JSON to:", path)
            return False
    else:
        print("No manufacturer found in security data for:", path)
        return False
    
def main():
    print(f"Resolved DATA_PATH: {DATA_PATH}")
    files = list(DATA_PATH.glob("**/data.json"))

    updated_count = 0
    scanned_count = 0
    for file_path in files:
        scanned_count += 1
        if updateFile(file_path):
            updated_count += 1

    print(f"Scanned {scanned_count} files, updated {updated_count} files.")

if __name__ == "__main__":
    main()
