# Go thrue all resoults/HardPc.pl look for webp files and convert them to png
import os
from pathlib import Path
from PIL import Image

BASE_PATH = Path(__file__).resolve().parent.resolve()
DATA_PATH = BASE_PATH / "resoult" / "Hard-PC.pl"

def convert_webp_to_png(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = Path(root) / file
                png_path = webp_path.with_suffix('.png')
                
                try:
                    with Image.open(webp_path) as img:
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGBA')
                        else:
                            img = img.convert('RGB')
                        
                        img.save(png_path, 'PNG', icc_profile=None)
                    print(f"Converted: {webp_path} -> {png_path}")

                    if png_path.stat().st_size > 2 * 1024 * 1024:
                        with Image.open(png_path) as img:
                            img = img.resize((img.width // 2, img.height // 2))
                            img.save(png_path, 'PNG', icc_profile=None)
                        print(f"Resized: {png_path} to reduce size")

                except Exception as e:
                    print(f"Failed to convert {webp_path}: {e}")

print("Starting conversion of WEBP to PNG...")
print(f"Target directory: {DATA_PATH}")
convert_webp_to_png(DATA_PATH)