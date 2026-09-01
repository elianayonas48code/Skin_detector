from pathlib import Path

DATASET = Path("../dataset")

CLASSES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]

SPLITS = [
    "train",
    "validation",
    "test"
]

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}

grand_total = 0

for split in SPLITS:

    print()
    print("=" * 30)
    print(split.upper())
    print("=" * 30)

    split_total = 0

    for class_name in CLASSES:

        folder = DATASET / split / class_name

        count = sum(
            1
            for file in folder.iterdir()
            if file.suffix.lower() in IMAGE_EXTENSIONS
        )

        print(f"{class_name}: {count}")

        split_total += count

    print(f"Total {split}: {split_total}")

    grand_total += split_total

print()
print("=" * 30)
print(f"GRAND TOTAL: {grand_total}")
print("=" * 30)