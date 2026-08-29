import pandas as pd
from pathlib import Path

metadata_path = Path("ham10000/HAM10000_metadata.csv")

image_folders = [
    Path("ham10000/HAM10000_images_part_1"),
    Path("ham10000/HAM10000_images_part_2")
]

df = pd.read_csv(metadata_path)

classes = sorted(df["dx"].unique())

print("=" * 40)
print("HAM10000 DATASET CHECK")
print("=" * 40)

print("Total metadata rows:", len(df))
print("Classes:", classes)
print("Number of classes:", len(classes))

print()
print("Images by class in the metadata:")
print(df["dx"].value_counts())

print()
print("Checking image files...")

found = 0
missing = 0

for image_id in df["image_id"]:

    image_found = False

    for folder in image_folders:

        image_path = folder / f"{image_id}.jpg"

        if image_path.exists():
            image_found = True
            break

    if image_found:
        found += 1
    else:
        missing += 1

print()
print("Images found:", found)
print("Images missing:", missing)

print("=" * 40)