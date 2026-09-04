from flask import Flask, render_template

app = Flask(__name__)


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


# Start Flask
if __name__ == "__main__":
    app.run(debug=True)