from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as img
from tensorflow import keras

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
SIZE = 64 
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
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
          message = "Flooding"
    else:
          message = "No Flooding"

# Example usage
image_path = request.form['file']
file.save("uploade.jpg")
upload_image(image_path)
plt.figure(figsize=(7, 7))
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE))
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run(debug=True)