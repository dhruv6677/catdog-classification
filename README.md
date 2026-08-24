# 🐱🐶 Object Classifier - Cat vs Dog using CNN

A deep learning project that classifies images of **Cats** and **Dogs** using a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras**.

---

## 📸 Project Demo
Deployed Link:- https://catdog-classification-lif4.onrender.com/

<img src="/output.png" width="700">

---

# 🚀 Features

* Binary Classification: **Cat vs Dog**
* Image preprocessing and augmentation
* CNN model built with TensorFlow/Keras
* Train, validate, and test workflow
* Predict custom images
* Save and load trained model
* GPU support for faster training

---

# 🛠️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📂 Dataset

Download the dataset from Kaggle:

[https://www.kaggle.com/c/dogs-vs-cats/data](https://www.kaggle.com/c/dogs-vs-cats/data)

After downloading, organize the dataset in the following structure:

```bash
dataset/
│
├── train/
│   ├── cats/
│   └── dogs/
│
└── test/
    ├── cats/
    └── dogs/
```

---

# 📁 Project Structure

```bash
object-classifier/
│
├── cats_and_dogs_filtered/    # Dataset folder
├── output.png                 # Demo output image
├── CNN.py                     # Model training script
├── evaluate.py                # Model evaluation script
├── predict.py                 # Predict custom image
├── model.h5                   # Saved trained model
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone <repository_url>
cd object-classifier
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Prepare Dataset

Place all training and testing images inside:

```bash
dataset/
├── train/
│   ├── cats/
│   └── dogs/
└── test/
    ├── cats/
    └── dogs/
```

---

# 🧠 Train the Model

Run the training script:

```bash
python CNN.py
```

### Output

* Training accuracy and loss per epoch
* Saved trained model:

```bash
model.h5
```

---

# 📊 Evaluate the Model

Run:

```bash
python evaluate.py
```

This evaluates the model on test images and prints:

* Test Accuracy
* Test Loss

---

# 🔍 Predict Custom Images

Run:

```bash
python predict.py --image_path path_to_image.jpg
```

### Example

```bash
python predict.py --image_path images/cat.jpg
```

### Sample Output

```bash
Prediction: Cat
Confidence: 98.4%
```

---

# 🧱 CNN Model Architecture

The CNN model contains:

* 3 Convolutional Layers
* ReLU Activation Function
* MaxPooling Layers
* Flatten Layer
* Dense Layers
* Dropout Layer
* Sigmoid Output Layer

---

# 📈 Data Augmentation

To improve model generalization, the following augmentations are used:

* Rescaling
* Rotation
* Zoom
* Horizontal Flip
* Shear Transformation

---

# ⚡ GPU Support

Training on GPU is highly recommended for faster performance.

Check GPU availability:

```python
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
```

---

# 🔧 Hyperparameters

Modify these values inside `CNN.py`:

```python
BATCH_SIZE = 32
EPOCHS = 10
IMAGE_SIZE = 128
LEARNING_RATE = 0.001
```

---

# 📦 Save & Load Model

## Save Model

```python
model.save("model.h5")
```

## Load Model

```python
from tensorflow.keras.models import load_model

model = load_model("model.h5")
```

---

# 📝 Notes

* Data augmentation helps reduce overfitting
* Increase epochs for better accuracy
* Use GPU for faster training
* Larger datasets improve performance

---

# 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* OpenCV
* Matplotlib

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
