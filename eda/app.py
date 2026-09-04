from flask import Flask, render_template, request
import os

from model.predict import load_model, predict_image


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Load the CNN model once when the app starts
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

    if "image" not in request.files:
        return "No image uploaded", 400

    image = request.files["image"]

    if image.filename == "":
        return "No image selected", 400

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)

    try:

        result = predict_image(
            model,
            image_path
        )

        return render_template(
            "result.html",
            result=result,
            image_path=image_path
        )

    except Exception as error:

        return f"Prediction error: {error}", 500


if __name__ == "__main__":
    app.run(debug=True)
