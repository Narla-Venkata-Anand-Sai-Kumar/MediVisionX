from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, UnidentifiedImageError
import numpy as np
from classify import classify  # Import classify function from classify.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('home', error="No file part in the request."))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home', error="No selected file."))

    try:
        img = Image.open(file.stream).convert('RGB')
        img_array = np.array(img)
        prediction = classify(img_array)
    except UnidentifiedImageError:
        return redirect(url_for('home', error="Invalid image file. Please upload a valid image."))
    except Exception as e:
        return redirect(url_for('home', error="An error occurred during prediction."))

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5100)
