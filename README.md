# Computer Vision Project

This repository contains a collection of various computer vision projects that demonstrate different techniques and methods for image and video processing using OpenCV and other libraries.

## Project 1: Face Detection using Haar-Cascade

### Overview
This project is a simple face detection application that uses the Haar-Cascade method. It leverages OpenCV's `haarcascade_frontalface_default.xml` file to detect faces in real-time via a webcam feed. The program identifies facial features and draws bounding boxes around detected faces.

### Features
- **Real-time Face Detection**: The program processes live video feed from the webcam to detect faces.
- **Bounding Boxes**: It draws a red bounding box around each detected face in the video stream.
- **Face Count**: The total number of detected faces is displayed on the screen in real-time.

### How It Works
1. **Haar-Cascade Classifier**: The project utilizes a pre-trained Haar-Cascade classifier, `haarcascade_frontalface_default.xml`, provided by OpenCV. This classifier is used to detect the frontal view of human faces.
2. **Grayscale Conversion**: The video frames are converted to grayscale to simplify the detection process, as the Haar-Cascade classifier operates on single-channel images.
3. **Detection and Bounding Boxes**: The classifier identifies faces in the grayscale image, and the program draws bounding boxes around them. The number of detected faces is also displayed.

### Requirements
- Python 3.x
- OpenCV

### Project Structure

computer-vision-project/
│
├── face-detection/
│   ├── cascade_container/
│   │   └── haarcascade_frontalface_default.xml
│   ├── face_detection.py
│   
│
└── README.md

### Future Projects
This repository will be updated with more computer vision projects in the future. Stay tuned for additional implementations of various techniques and algorithms in the field of computer vision.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
