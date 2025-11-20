import json
import os
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.resolve()
DATA_PATH = BASE_PATH / "resoult"
OUT = BASE_PATH / "manufacturers.json"

def main():
    manufacturers = {}
    for dirpath, _, filenames in os.walk(DATA_PATH):
        for fn in filenames:
            if fn.lower() != "data.json":
                continue
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                continue
            manufacturer = data.get("manufacturer")
            if not manufacturer:
                continue
            if manufacturer not in manufacturers:
                print("Processing manufacturer:", manufacturer)
                manufacturers[manufacturer] = []
                
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(manufacturers, f, ensure_ascii=False, indent=2)
    print("Wrote:", OUT)

if __name__ == "__main__":  
    main()