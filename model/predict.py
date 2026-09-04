import os
import sys

import numpy as np
import tensorflow as tf


# ============================================================
# MODEL SETTINGS
# ============================================================

# Get the project directory reliably
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the trained CNN model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "skin_cancer_cnn_original.keras"
)

# Image size expected by the CNN
IMG_SIZE = (224, 224)


# ============================================================
# CLASS INFORMATION
# ============================================================

CLASS_NAMES = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc"
]


CLASS_LABELS = {
    "akiec": "Actinic Keratoses",
    "bcc": "Basal Cell Carcinoma",
    "bkl": "Benign Keratosis",
    "df": "Dermatofibroma",
    "mel": "Melanoma",
    "nv": "Melanocytic Nevi",
    "vasc": "Vascular Lesions"
}


# ============================================================
# GENERAL SKIN HEALTH ADVICE
# ============================================================

ADVICE = {

    "akiec": (
        "Protect your skin from excessive sun exposure and use "
        "sunscreen. Consider having the lesion assessed by a "
        "qualified healthcare professional."
    ),

    "bcc": (
        "Protect your skin from excessive sun exposure and monitor "
        "the area for changes. Suspicious or changing lesions should "
        "be assessed by a qualified healthcare professional."
    ),

    "bkl": (
        "Continue monitoring the area for changes in size, shape, "
        "color, or symptoms. If it changes or concerns you, consult "
        "a qualified healthcare professional."
    ),

    "df": (
        "Monitor the area for changes in appearance, size, or "
        "symptoms. If you are concerned about the lesion, seek "
        "professional medical advice."
    ),

    "mel": (
        "This prediction should be taken seriously. The lesion should "
        "be assessed by a qualified healthcare professional. Do not "
        "rely on the AI prediction alone."
    ),

    "nv": (
        "Continue monitoring the area for changes in size, shape, "
        "color, or appearance. If you notice significant changes or "
        "have concerns, consult a qualified healthcare professional."
    ),

    "vasc": (
        "Monitor the area for changes. If the lesion is changing, "
        "painful, bleeding, or concerning, seek advice from a "
        "qualified healthcare professional."
    )
}


# ============================================================
# LOAD MODEL
# ============================================================

def load_model():
    """
    Load the trained CNN model.
    """

    print("Loading CNN model...")

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found:\n{MODEL_PATH}"
        )

    model = tf.keras.models.load_model(MODEL_PATH)

    print("Model loaded successfully.")

    return model


# ============================================================
# PREDICT IMAGE
# ============================================================

def predict_image(model, image_path):
    """
    Predict the skin-disease class of an image.

    Returns a dictionary containing:
    - predicted class
    - condition name
    - confidence
    - advice
    - probabilities for all seven classes
    """

    # Check that image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    # --------------------------------------------------------
    # Load and resize image
    # --------------------------------------------------------

    image = tf.keras.utils.load_img(
        image_path,
        target_size=IMG_SIZE
    )

    # Convert image to NumPy array
    image_array = tf.keras.utils.img_to_array(image)

    # Add batch dimension
    image_array = tf.expand_dims(
        image_array,
        axis=0
    )

    # --------------------------------------------------------
    # Make prediction
    # --------------------------------------------------------

    predictions = model.predict(
        image_array,
        verbose=0
    )[0]

    # Find class with highest probability
    predicted_index = int(np.argmax(predictions))

    predicted_class = CLASS_NAMES[predicted_index]

    # Convert probability to percentage
    confidence = float(
        predictions[predicted_index] * 100
    )

    # --------------------------------------------------------
    # Get all class probabilities
    # --------------------------------------------------------

    probabilities = {}

    for index, class_name in enumerate(CLASS_NAMES):

        probability = float(
            predictions[index] * 100
        )

        probabilities[CLASS_LABELS[class_name]] = round(
            probability,
            2
        )

    # --------------------------------------------------------
    # Build result
    # --------------------------------------------------------

    result = {
        "class": predicted_class,

        "condition": CLASS_LABELS[predicted_class],

        "confidence": round(
            confidence,
            2
        ),

        "advice": ADVICE[predicted_class],

        "probabilities": probabilities
    }

    return result


# ============================================================
# COMMAND-LINE TEST
# ============================================================

if __name__ == "__main__":

    # Check that an image path was provided
    if len(sys.argv) < 2:

        print()
        print("Please provide an image path.")
        print()
        print("Example:")
        print(
            "python model/predict.py path/to/image.jpg"
        )

        sys.exit(1)

    # Get image path from command line
    image_path = sys.argv[1]

    try:

        # Load CNN model
        model = load_model()

        # Predict image
        result = predict_image(
            model,
            image_path
        )

        # ----------------------------------------------------
        # Display results
        # ----------------------------------------------------

        print()
        print("Prediction Results")
        print("==================")

        print(
            "Class:",
            result["class"]
        )

        print(
            "Condition:",
            result["condition"]
        )

        print(
            f"Confidence: "
            f"{result['confidence']:.2f}%"
        )

        print()
        print("All Class Probabilities")
        print("=======================")

        for condition, probability in result[
            "probabilities"
        ].items():

            print(
                f"{condition}: "
                f"{probability:.2f}%"
            )

        print()
        print("General Skin Health Advice")
        print("==========================")

        print(result["advice"])

        print()
        print("IMPORTANT:")
        print(
            "This AI result is not a medical diagnosis and "
            "should not replace professional medical advice."
        )

    except Exception as error:

        print()
        print("Prediction Error")
        print("================")

        print(error)
