from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

from model.predict import load_model, predict_image

app = Flask(__name__)

# Folder where uploaded images will be stored
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the CNN model once when Flask starts
model = load_model()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Skin detection page
@app.route("/detect")
def detect():
    return render_template("detect.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# How It Works page
@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image was uploaded."}), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "No image was selected."}), 400

    filename = secure_filename(image.filename)
    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(image_path)

    try:
        result = predict_image(model, image_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Start Flask
if __name__ == "__main__":
    app.run(debug=True)