from pathlib import Path
from PIL import Image
import random

# Where our dataset is located
DATASET = Path("../dataset")

# Our 7 HAM10000 classes
CLASSES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]

# Number of dummy images for each class
IMAGES_PER_CLASS = 20

# Image size
IMAGE_SIZE = (224, 224)

# Make the results repeatable
random.seed(42)


def create_dummy_image(path):
    """Create one simple dummy RGB image."""

    pixels = []

    for _ in range(IMAGE_SIZE[0] * IMAGE_SIZE[1]):
        r = random.randint(50, 220)
        g = random.randint(50, 220)
        b = random.randint(50, 220)

        pixels.append((r, g, b))

    image = Image.new("RGB", IMAGE_SIZE)
    image.putdata(pixels)

    image.save(path)


# Create images in train, validation, and test
for split in ["train", "validation", "test"]:

    for class_name in CLASSES:

        folder = DATASET / split / class_name
        folder.mkdir(parents=True, exist_ok=True)

        for number in range(IMAGES_PER_CLASS):

            image_path = folder / f"dummy_{number + 1}.jpg"

            create_dummy_image(image_path)

print("Dummy dataset created successfully!")

print()
print("Classes:")

for number, class_name in enumerate(CLASSES):
    print(f"{number} = {class_name}")

print()
print("Image size: 224 x 224 RGB")
print("Images per class per split:", IMAGES_PER_CLASS)