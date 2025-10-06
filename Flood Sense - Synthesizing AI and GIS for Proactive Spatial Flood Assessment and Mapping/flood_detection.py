from flask import Flask, render_template, request, send_from_directory
import cv2
import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as img
from tensorflow import keras

UPLOAD_FOLDER = 'uploads'
SIZE = 64  # Update the SIZE to match the expected input shape
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load the trained model
model = keras.models.load_model('flooding1.h5')

categories = ["Flooding", "No Flooding"]

def upload_image(file_path):
    nimage = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(nimage, (SIZE, SIZE))  # Resize the image to (64, 64)
    image = image / 255.0
    prediction = model.predict(np.array(image).reshape(-1, SIZE, SIZE, 1))
    pclass = np.argmax(prediction)
    print(prediction)
    print(pclass)
    pValue = "The Signature is: {0}".format(categories[int(pclass)])
    print(pValue)
    realvalue = "Real Value 1"
    print('Success')
    if pclass == 0:
          print("Flooding")
    else:
          print("No Flooding")

# Example usage
image_path = request.form['file']
file.save("uploade.jpg")
upload_image(image_path)
plt.figure(figsize=(7, 7))
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE))