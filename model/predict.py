import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "model/skin_cancer_cnn_original.keras"
IMG_SIZE = (224, 224)

CLASS_NAMES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]

print("Loading CNN model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("CNN model loaded successfully.")


def predict_skin_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(IMG_SIZE)

    image_array = np.array(image, dtype=np.float32)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)[0]

    predicted_index = np.argmax(predictions)
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(predictions[predicted_index])

    return {
        "class": predicted_class,
        "confidence": confidence,
        "probabilities": {
            CLASS_NAMES[i]: float(predictions[i])
            for i in range(len(CLASS_NAMES))
        }
    }


if __name__ == "__main__":
    print("CNN prediction module is ready.")