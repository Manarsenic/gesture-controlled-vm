# Gesture Controlled Virtual Mouse - Complete Setup Guide

This guide documents the complete installation process required to run the project on a modern Windows system.

---

# Prerequisites

### Hardware

* Webcam
* Windows 10/11
* Internet Connection

### Software

* Python 3.8.5

The project was originally developed using Python 3.8 and several dependencies do not work correctly on Python 3.12+ and Python 3.13.

---

# Step 1 - Download Project

Clone repository:

```bash
git clone <repository-url>
```

or download ZIP and extract.

---

# Step 2 - Install Python 3.8.5

Download:

https://www.python.org/downloads/release/python-385/

Important:

* Enable "Add Python 3.8 to PATH"
* Complete installation

Verify:

```bash
py -3.8 --version
```

Expected:

```text
Python 3.8.5
```

---

# Step 3 - Create Virtual Environment

Open terminal in project root.

```bash
py -3.8 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Expected:

```text
(venv)
```

---

# Step 4 - Upgrade Pip

```bash
python -m pip install --upgrade pip setuptools wheel
```

---

# Step 5 - Fix requirements.txt

Original repository contains:

```text
mediapipe==0.8.6.2
```

Replace with:

```text
mediapipe==0.10.11
```

---

# Step 6 - Install Dependencies

```bash
pip install -r requirements.txt
```

Wait for installation to complete.

---

# Step 7 - Fix OpenCV

If OpenCV import errors occur:

```bash
pip uninstall opencv-python -y
pip uninstall opencv-contrib-python -y
```

Install stable version:

```bash
pip install opencv-python==4.5.5.64
```

Verify:

```bash
python -c "import cv2; print(cv2.__version__)"
```

Expected:

```text
4.5.5
```

---

# Step 8 - Enable Program Entry Point

Open:

```text
src/Gesture_Controller.py
```

At the bottom of the file:

Original:

```python
# gc1 = GestureController()
# gc1.start()
```

Change to:

```python
gc1 = GestureController()
gc1.start()
```

Without this change the application exits immediately.

---

# Step 9 - Run Gesture Controller

Navigate to:

```bash
cd src
```

Run:

```bash
python Gesture_Controller.py
```

Expected:

* Webcam opens
* Hand landmarks appear
* Gesture recognition starts

---

# Step 10 - Run Voice Assistant

```bash
python Proton.py
```

---

# Troubleshooting

## Error: No matching distribution found for mediapipe

Update:

```text
mediapipe==0.10.11
```

and reinstall requirements.

---

## Error: cv2 import failure

Run:

```bash
pip uninstall opencv-python -y
pip uninstall opencv-contrib-python -y
pip install opencv-python==4.5.5.64
```

---

## Webcam Not Opening

Check:

* Camera permissions enabled
* No other application using webcam
* Camera index set correctly

Test camera:

```python
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

print(ret)

cap.release()
```

Expected:

```text
True
```

---

# Project Structure

```text
Gesture-Controlled-Virtual-Mouse
│
├── README.md
├── SETUP_GUIDE.md
├── requirements.txt
│
├── src
│   ├── Gesture_Controller.py
│   ├── Gesture_Controller_Gloved.py
│   ├── Proton.py
│   ├── app.py
│   ├── calib_images
│   └── web
│
└── venv
```

---

# Notes

This guide includes fixes required to run the original repository on modern Windows systems.

Main fixes:

* Python 3.8 installation
* MediaPipe dependency update
* OpenCV compatibility fix
* Enabling application startup code
