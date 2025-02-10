# MediVisionX

**MediVisionX** is a medical image classification web application that uses deep learning models to classify medical images and provide diagnostic insights. The application is built using Flask for the backend, TensorFlow for model handling, and OpenCV for image processing.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Models Used](#models-used)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Medical Image Upload**: Upload medical images for analysis.
- **Image Classification**: Models classify images into various diagnostic categories, like bone fractures, brain conditions, and more.
- **Intuitive Interface**: Elegant and modern UI with a glassy, user-friendly design.
- **Real-Time Predictions**: Instant classification results upon image upload.

## Project Structure

The project is organized into the following structure:

```plaintext
Health-Vision/
├── models/                  # Pre-trained deep learning models for each medical condition
│   ├── all-in-one.h5
│   ├── brain.h5
│   ├── chest.h5
│   ├── eye.h5
│   ├── fracture.h5
│   ├── kidney.h5
│   └── skin.h5
├── app.py                   # Main application file for Flask
├── classify.py              # Script with classification logic using the models
├── static/                  # Static files (CSS, images)
│   └── css/
│       └── styles.css       # Main stylesheet for the application
├── templates/               # HTML templates for Flask
│   ├── base.html            # Base HTML template with header and footer
│   └── index.html           # Main page template
├── README.md                # Project documentation
└── requirements.txt         # List of Python dependencies
```

## Models Used

Each model specializes in a specific diagnostic category:
- **All-in-One Model**: General model to classify broad categories of images.
- **Fracture Model**: Detects fractures in bone images.
- **Brain Model**: Classifies brain conditions (e.g., pituitary, glioma).
- **Chest Model**: Detects pneumonia in chest X-rays.
- **Eye Model**: Identifies eye conditions (e.g., glaucoma, cataract).
- **Kidney Model**: Detects kidney conditions (e.g., cyst, tumor).
- **Skin Model**: Classifies skin lesions and conditions.

## Installation

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/Narla-Venkata-Anand-Sai-Kumar/MediVisionX.git
cd MediVisionX
```

### 🚀 **1. Build the Docker Image**  
```bash
docker build -t medvisionx .
```
- `-t medvisionx` tags the image with the name `medvisionx`.
- `.` specifies the current directory as the build context.

---

### ⚡ **2. Run the Docker Container**  
```bash
docker run -d -p 5100:5100 --name medvisionx-container medvisionx
```
- `-d` runs the container in detached mode (in the background).
- `-p 5100:5100` maps port `5100` on your machine to port `5100` in the container.
- `--name medvisionx-container` gives the container a recognizable name.
- `medvisionx` is the image name you built earlier.

---

### ✅ **3. Verify the Running Container**  
```bash
docker ps
```
This shows active containers. You should see `medvisionx-container` running.

---

### 📊 **4. Check Container Logs (Optional)**  
```bash
docker logs medvisionx-container
```
This helps if you want to debug any output or errors.

---

### 🛑 **5. Stop and Remove the Container (If Needed)**  
```bash
docker stop medvisionx-container
docker rm medvisionx-container
```

### Access the Application

Open a web browser and go to:

```plaintext
http://127.0.0.1:5000
```

### Upload and Classify an Image

1. On the homepage, upload a medical image (e.g., an X-ray).
2. Click the "Classify Image" button.
3. The application will process the image and display a classification result.

### Example Prediction Categories

After uploading an image, Health-Vision will classify the image into a category (e.g., "fractured," "pituitary tumor") depending on the model's result.

## Technologies Used

- **Flask**: Web framework for serving the application.
- **TensorFlow**: Machine learning framework for loading and running models.
- **OpenCV**: Library for image processing and manipulation.
- **NumPy**: For efficient numerical operations.
- **Pillow**: Python Imaging Library for handling images.

### Potential Errors and Solutions

1. **Error loading model files**: Ensure all model files are placed in the `models/` directory.
2. **Environment compatibility issues**: Ensure Python and TensorFlow versions match the requirements.

## Contributing

If you'd like to contribute to Health-Vision:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

All contributions, issues, and feature requests are welcome!

## Team

- [NARLA VENKATA ANAND SAI KUMAR](https://github.com/Narla-Venkata-Anand-Sai-Kumar/)
- [KARTHIK TARAKA SAI BOLLA](https://github.com/karthikbolla)

## License

This project is licensed under the MIT License.

---

### Note
**Health-Vision** is intended for educational and research purposes only. It should not be used as a replacement for professional medical advice or diagnostics.
