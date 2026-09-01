from pathlib import Path
from PIL import Image
import numpy as np

# Choose one image
image_path = Path("dataset/train/akiec/dummy_1.jpg")

# Open image
image = Image.open(image_path)

# Convert to RGB
image = image.convert("RGB")

# Resize
image = image.resize((224, 224))

# Convert to NumPy array
image_array = np.array(image)

# Convert pixel values from 0-255 to 0-1
normalized_image = image_array / 255.0

print("Image shape:", normalized_image.shape)

print("Minimum pixel value:", normalized_image.min())
print("Maximum pixel value:", normalized_image.max())

print("First pixel before normalization:",
      image_array[0, 0])

print("First pixel after normalization:",
      normalized_image[0, 0])