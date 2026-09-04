from flask import Flask, render_template, request, jsonify
import os

from model.predict import load_model, predict_image


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Load the CNN model once when the application starts
print("Loading CNN model...")

model = load_model()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect")
def detect():
    return render_template("detect.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Check if an image was uploaded
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded."
        }), 400

    image = request.files["image"]

    # Check if a file was actually selected
    if image.filename == "":
        return jsonify({
            "error": "No image selected."
        }), 400

    # Save uploaded image
    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)

    try:

        # Run CNN prediction
        result = predict_image(
            model,
            image_path
        )

        # Send prediction back to detect.html
        return jsonify(result)

    except Exception as error:

        print("Prediction error:", error)

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
