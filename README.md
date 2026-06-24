# Gesture Controlled Virtual Mouse

A computer vision-based Human Computer Interaction system that enables users to control their computer using hand gestures and voice commands.

## Features

### Hand Gesture Recognition

* Real-time hand tracking using MediaPipe
* Cursor movement using index finger
* Left Click
* Right Click
* Double Click
* Drag and Drop
* Scrolling
* Multiple Item Selection

### System Controls

* Volume Control
* Brightness Control

### Voice Assistant (Proton)

* Launch Gesture Recognition
* Google Search
* Location Search using Google Maps
* File Navigation
* Copy & Paste Operations
* Date and Time Queries
* Voice Commands

## Technologies Used

### Computer Vision

* OpenCV
* MediaPipe

### Python Libraries

* PyAutoGUI
* PyCaw
* SpeechRecognition
* Pyttsx3
* Screen Brightness Control
* Eel

## Project Structure

```text
src/
│
├── Gesture_Controller.py
├── Gesture_Controller_Gloved.py
├── Proton.py
├── app.py
│
├── calib_images/
│   └── checkerboard/
│
└── web/
    ├── css/
    ├── images/
    ├── js/
    └── index.html
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd gesture-controlled-virtual-mouse
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Project

Navigate to:

```bash
cd src
```

Run Gesture Controller:

```bash
python Gesture_Controller.py
```

Run Voice Assistant:

```bash
python Proton.py
```

## Working Principle

1. Webcam captures video frames.
2. OpenCV processes frames.
3. MediaPipe detects 21 hand landmarks.
4. Gesture recognition logic interprets finger positions.
5. Corresponding mouse or system actions are executed.

## Applications

* Touchless Computer Interaction
* Accessibility Systems
* Smart Workstations
* Human Computer Interaction Research
* Gesture-Based Automation

## Future Improvements

* AI-based gesture classification
* Dynamic gesture recognition using deep learning
* Custom gesture training
* Multi-user support
* Cross-platform compatibility
