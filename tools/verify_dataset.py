from pathlib import Path
from PIL import Image

DATASET_DIR = Path("../dataset")

splits = ["train", "validation", "test"]

total_images = 0
bad_images = 0

print("=" * 50)
print("FINAL DATASET VERIFICATION")
print("=" * 50)

for split in splits:

    print()
    print(split.upper())

    split_total = 0

    split_folder = DATASET_DIR / split

    for class_folder in sorted(split_folder.iterdir()):

        if not class_folder.is_dir():
            continue

        class_count = 0

        for image_path in class_folder.glob("*.jpg"):

            try:
                with Image.open(image_path) as image:
                    image.verify()

                class_count += 1

            except Exception:
                print("BAD IMAGE:", image_path)
                bad_images += 1

        print(f"{class_folder.name}: {class_count}")

        split_total += class_count

    print(f"Total {split}: {split_total}")

    total_images += split_total

print()
print("=" * 50)
print("TOTAL IMAGES:", total_images)
print("BAD IMAGES:", bad_images)
print("=" * 50)