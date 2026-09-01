import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import shutil

# ==========================================
# SETTINGS
# ==========================================

METADATA_FILE = Path("../ham10000/HAM10000_metadata.csv")

IMAGE_FOLDERS = [
    Path("../ham10000/HAM10000_images_part_1"),
    Path("../ham10000/HAM10000_images_part_2"),
]

OUTPUT_DIR = Path("../dataset")

CLASSES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc",
]

RANDOM_STATE = 42


# ==========================================
# READ METADATA
# ==========================================

print("Reading metadata...")

df = pd.read_csv(METADATA_FILE)

print(f"Total images in metadata: {len(df)}")


# ==========================================
# FIND IMAGE FUNCTION
# ==========================================

def find_image(image_id):
    for folder in IMAGE_FOLDERS:

        image_path = folder / f"{image_id}.jpg"

        if image_path.exists():
            return image_path

    return None


# ==========================================
# CREATE OUTPUT FOLDERS
# ==========================================

for split in ["train", "validation", "test"]:

    for class_name in CLASSES:

        folder = OUTPUT_DIR / split / class_name

        folder.mkdir(parents=True, exist_ok=True)


# ==========================================
# SPLIT DATA
# ==========================================

train_data, temp_data = train_test_split(
    df,
    test_size=0.30,
    stratify=df["dx"],
    random_state=RANDOM_STATE
)

validation_data, test_data = train_test_split(
    temp_data,
    test_size=0.50,
    stratify=temp_data["dx"],
    random_state=RANDOM_STATE
)


print()
print("Dataset split:")
print("----------------")
print("Training:", len(train_data))
print("Validation:", len(validation_data))
print("Testing:", len(test_data))


# ==========================================
# COPY FUNCTION
# ==========================================

def copy_images(data, split_name):

    print()
    print(f"Creating {split_name} dataset...")

    copied = 0
    missing = 0

    for _, row in data.iterrows():

        image_id = row["image_id"]
        class_name = row["dx"]

        source = find_image(image_id)

        if source is None:

            print(f"WARNING: Missing image {image_id}")
            missing += 1
            continue

        destination = (
            OUTPUT_DIR
            / split_name
            / class_name
            / f"{image_id}.jpg"
        )

        shutil.copy2(source, destination)

        copied += 1

    print(f"Copied: {copied}")
    print(f"Missing: {missing}")


# ==========================================
# COPY DATA
# ==========================================

copy_images(train_data, "train")

copy_images(validation_data, "validation")

copy_images(test_data, "test")


# ==========================================
# FINAL REPORT
# ==========================================

print()
print("=" * 50)
print("FINAL DATASET REPORT")
print("=" * 50)

total = 0

for split in ["train", "validation", "test"]:

    print()
    print(split.upper())

    split_total = 0

    for class_name in CLASSES:

        folder = OUTPUT_DIR / split / class_name

        count = len(list(folder.glob("*.jpg")))

        print(f"{class_name}: {count}")

        split_total += count

    print(f"Total {split}: {split_total}")

    total += split_total


print()
print("=" * 50)
print(f"TOTAL COPIED: {total}")
print("=" * 50)