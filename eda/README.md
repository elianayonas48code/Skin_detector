# 🩺 Skin Detector — AI-Powered Skin Lesion Classification

Skin Detector is an AI-powered web application designed to classify skin lesion images into one of seven categories using a Convolutional Neural Network (CNN). The system provides a simple interface where users can upload an image and receive an AI-generated prediction.

> **Important:** Skin Detector is an educational and research project. It is **not a medical diagnostic tool** and should not be used as a substitute for examination or advice from a qualified healthcare professional.

---

## 📌 Project Overview

Skin diseases and skin lesions can have similar visual characteristics, making classification challenging. This project explores how artificial intelligence and deep learning can be used to assist with the classification of skin lesion images.

The application combines:

* A skin lesion image dataset
* Image preprocessing
* A CNN-based machine learning model
* A Flask backend
* An HTML/CSS/JavaScript frontend
* A prediction interface for users

### Basic workflow

```text
User
  ↓
Upload Skin Lesion Image
  ↓
Image Preprocessing
  ↓
CNN Model
  ↓
Prediction
  ↓
Predicted Class + Confidence
  ↓
Result Display
```

---

# 📊 Dataset

## HAM10000

The project uses the **HAM10000 ("Human Against Machine with 10000 training images") dataset**, a publicly available dataset of dermatoscopic images of pigmented skin lesions.

The dataset contains approximately **10,015 images** distributed across seven diagnostic categories.

### Dataset Classes

| Code    | Class                                           |
| ------- | ----------------------------------------------- |
| `akiec` | Actinic keratoses and intraepithelial carcinoma |
| `bcc`   | Basal cell carcinoma                            |
| `bkl`   | Benign keratosis-like lesions                   |
| `df`    | Dermatofibroma                                  |
| `mel`   | Melanoma                                        |
| `nv`    | Melanocytic nevi                                |
| `vasc`  | Vascular lesions                                |

### Dataset Distribution

The original dataset contains an imbalanced number of images among the seven classes.

Approximate distribution:

| Class     |     Images |
| --------- | ---------: |
| `nv`      |      6,705 |
| `mel`     |      1,113 |
| `bkl`     |      1,099 |
| `bcc`     |        514 |
| `akiec`   |        327 |
| `vasc`    |        142 |
| `df`      |        115 |
| **Total** | **10,015** |

The images were organized into training, validation, and testing sets for model development and evaluation.

### Dataset Considerations

The dataset is imbalanced, meaning some classes contain significantly more images than others. This is an important consideration when evaluating model performance because overall accuracy alone may not represent how well the model performs on less-represented classes.

---

# 🤖 Machine Learning Model

The project uses a **Convolutional Neural Network (CNN)** for image classification.

CNNs are commonly used for image-recognition tasks because they can learn visual patterns such as:

* Edges
* Shapes
* Textures
* Color patterns
* More complex visual features

The model receives a processed skin lesion image and produces predictions for the seven classes in the dataset.

### Model Pipeline

```text
Input Image
     ↓
Image Resizing
     ↓
Pixel Preprocessing
     ↓
CNN
     ↓
Feature Extraction
     ↓
Classification Layer
     ↓
7 Class Predictions
```

The trained model is saved as a `.keras` model and is loaded by the Flask application when predictions are requested.

---

# 🧠 Prediction Process

When a user uploads an image:

1. The Flask application receives the uploaded image.
2. The image is validated.
3. The image is resized to the dimensions expected by the model.
4. Pixel values are preprocessed.
5. The processed image is passed to the CNN.
6. The model generates probabilities for the seven classes.
7. The class with the highest predicted probability is selected.
8. The prediction is displayed on the results page.

The application also provides a confidence value associated with the model's prediction.

> A model confidence score represents the model's estimated probability for its prediction. It should **not** be interpreted as the probability that the user actually has a particular disease.

---

# 💻 Technologies Used

## Programming Languages

* **Python**
* **HTML**
* **CSS**
* **JavaScript**

## Machine Learning

* **TensorFlow**
* **Keras**
* Convolutional Neural Networks (CNN)

## Backend

* **Flask**

Flask is used to create the web server, handle image uploads, connect the frontend to the machine-learning model, and return prediction results.

## Frontend

* HTML
* CSS
* JavaScript

The frontend provides the user interface for uploading images and viewing predictions.

## Development Tools

* PyCharm
* Git
* GitHub

---

# 📁 Project Structure

The project is organized approximately as follows:

```text
Skin_detector/
│
├── app.py
├── main.py
│
├── model/
│   └── model.keras
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── detect.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── tools/
│   ├── check_dataset.py
│   ├── check_ham10000.py
│   ├── create_dummy_dataset.py
│   ├── organize_dataset.py
│   ├── test_image.py
│   ├── test_tensorflow.py
│   └── verify_dataset.py
│
├── classes.txt
├── dataset_info.txt
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact files and folders may vary depending on the final version of the project.

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/elianayonas48code/Skin_detector.git
```

Move into the project directory:

```bash
cd Skin_detector
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project requires packages such as:

```text
Flask
TensorFlow
Keras
NumPy
Pillow
```

The exact versions should be specified in `requirements.txt` for reproducibility.

---

# ▶️ Running the Application

After installing the dependencies, start the Flask application:

```bash
python app.py
```

The application will normally be available locally at:

```text
http://127.0.0.1:5000/
```

The detection page is available at:

```text
http://127.0.0.1:5000/detect
```

Open the address in a web browser and use the application to upload an image.

---

# 🖼️ Using the Application

### Step 1 — Open Skin Detector

Navigate to the application's homepage.

### Step 2 — Open Detection

Select the **Detect** option.

### Step 3 — Upload an Image

Upload a supported skin lesion image.

### Step 4 — Analyze

Submit the image for analysis.

### Step 5 — View Results

The application displays the model's predicted class and associated confidence.

---

# 🔬 Model Evaluation

Model performance should be evaluated using more than overall accuracy.

Recommended evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

Because the HAM10000 dataset is imbalanced, **per-class metrics are particularly important**.

For example, a model could achieve a relatively high overall accuracy while performing poorly on classes with fewer training examples.

The final project should report the actual metrics obtained from the trained model rather than using expected or estimated values.

---

# ⚠️ Limitations

Skin Detector has several important limitations.

## 1. Dataset Imbalance

The HAM10000 dataset contains significantly more examples of some classes than others. This can cause the model to perform better on common classes than rare classes.

## 2. Image Quality

Model performance can be affected by:

* Blurry images
* Poor lighting
* Low-resolution images
* Unusual camera angles
* Images that differ significantly from the training data

## 3. Dataset Generalization

The model was trained using a specific dataset. Images from different cameras, environments, populations, or clinical settings may produce different results.

## 4. AI Prediction Is Not Diagnosis

The model's output is a classification prediction, not a medical diagnosis.

A prediction should not be used to make decisions about treatment or medical care.

## 5. Limited Number of Classes

The system only predicts the seven categories represented in the HAM10000 dataset. A skin condition outside these categories may be incorrectly classified as one of the available classes.

## 6. Model Limitations

CNN models can learn patterns and biases present in their training data. High test accuracy does not guarantee reliable performance in every real-world situation.

---

# 🔐 Privacy Considerations

Users should avoid uploading images containing unnecessary personal information.

If the application is deployed publicly, appropriate security and privacy measures should be implemented for uploaded images, including:

* Secure file handling
* Appropriate file validation
* Temporary storage where possible
* Deletion of uploaded images when they are no longer required
* Protection against unauthorized access

---

# 🚀 Future Improvements

Possible future improvements include:

* Increasing the size and diversity of the training data
* Addressing class imbalance
* Using data augmentation
* Experimenting with transfer-learning architectures
* Improving rare-class performance
* Adding stronger image-quality checks
* Adding more detailed evaluation reports
* Improving mobile responsiveness
* Adding model explainability techniques
* Improving deployment scalability
* Adding automated testing
* Improving security for uploaded files

---

# 👥 Team Roles

The project was developed as a team with different responsibilities.

### Member 1 — Dataset & Preprocessing

Responsibilities include:

* Dataset collection
* Dataset verification
* Dataset organization
* Image preprocessing
* Train/validation/test preparation

### Member 2 — AI Model

Responsibilities include:

* CNN/model development
* Model training
* Model optimization
* Prediction functionality
* Saving the trained model

### Member 3 — EDA, Evaluation & Documentation

Responsibilities include:

* Exploratory data analysis
* Dataset visualizations
* Model evaluation
* Performance metrics
* Confusion matrix
* Documentation and reporting

### Member 4 — Flask & Frontend Integration

Responsibilities include:

* Flask application
* Frontend development
* Model integration
* Image upload functionality
* Prediction/results interface
* Deployment

---

# 📚 Conclusion

Skin Detector demonstrates how machine learning can be integrated into a web application to classify skin lesion images.

The project combines **dataset preparation, image preprocessing, CNN-based classification, Flask backend development, and frontend design** into one application.

Although the system can provide useful experimental predictions, it has important limitations and should be treated as an **educational/research project rather than a clinical diagnostic system**.

---

## 📄 License

This project is intended for educational and research purposes.

The HAM10000 dataset is subject to its own licensing and usage conditions. Users of this project should review the dataset's original terms before redistributing the dataset or derivative materials.

---

## 🙏 Acknowledgment

We acknowledge the creators and contributors of the HAM10000 dataset for providing the images and metadata used in this project.

