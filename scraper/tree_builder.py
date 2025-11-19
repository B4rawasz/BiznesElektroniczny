import json
import os
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.resolve()
DATA_PATH = BASE_PATH / "resoult"
OUT = BASE_PATH / "item_categories.json"

def main():
    items = {}
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
            cats = data.get("category") or []
            ref = items
            for cat in cats:
                if cat not in ref:
                    ref[cat] = {}

                ref = ref[cat]
                
                

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print("Wrote:", OUT)

if __name__ == "__main__":
    main()