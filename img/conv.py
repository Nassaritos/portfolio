import os
from PIL import Image

# Folder path where PNGs are stored
folder_path = "."

# Loop through files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        png_path = os.path.join(folder_path, filename)
        webp_path = os.path.join(folder_path, filename.replace(".png", ".webp"))

        with Image.open(png_path) as img:
            img = img.convert("RGBA")  # Preserve transparency if needed
            img.save(webp_path, "WEBP", quality=80, method=6)  # Quality can be adjusted

        print(f"Converted: {filename} → {webp_path}")
