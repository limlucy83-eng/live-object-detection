# 🎥 Live Object Detection & Tracing

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-8.0+-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A real-time object detection and tracking web application built with Streamlit, YOLOv8, and WebRTC. This application provides live video analysis directly from your webcam with instant object detection and counting capabilities.

---

## ✨ Features

- 🎯 **Real-time Detection**: Process video frames in real-time with minimal latency.
- 📊 **Object Counting**: Automatic counting of detected objects with on-screen display.
- 🎥 **WebRTC Integration**: Direct webcam access through browser using WebRTC.
- 🤖 **YOLOv8 Nano**: Lightweight yet powerful object detection model.
- 📱 **Responsive UI**: Clean, modern interface built with Streamlit.
- 🔄 **Object Tracking**: Persistent tracking of objects across frames.
- 💚 **Visual Feedback**: Bounding boxes and labels overlaid on video feed.

---

## 📋 Prerequisites

- Python 3.8 or higher
- Webcam
- Modern web browser (Chrome, Firefox, Edge, or Safari)
- pip package manager

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd live_objective
   Create a virtual environment (recommended)Bashpython -m venv venv
# Windows:
source venv/Scripts/activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install streamlit streamlit-webrtc ultralytics opencv-python av numpy

# Download the YOLOv8 model
# The model (yolov8n.pt) will automatically download upon first execution.

# 📁 Project Structure
# live_objective/
# ├── app.py              # Main application logic
# ├── requirements.txt    # List of dependencies
# ├── yolov8n.pt          # Model weights (auto-downloaded)
# └── README.md           # Project documentation

# 🎮 Usage
# Run the application:
streamlit run app.py

# Access the application:
# Navigate to http://localhost:8501 in your browser.
# Permissions: Allow browser access to your webcam when prompted.

# 💻 Code Overview
# Model Loading:
from ultralytics import YOLO
model = YOLO('yolov8n.pt')

# Video Frame Processing:
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    results = model.track(img, persist=True, conf=0.5)
    annotated_frame = results[0].plot()
    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

# 📦 Dependencies
# streamlit          ≥1.28.0   Web framework
# streamlit-webrtc   ≥0.47.0   Video streaming
# ultralytics        ≥8.0.0    YOLOv8 detection
# opencv-python      ≥4.8.0    Image processing
# av                 ≥10.0.0   PyAV frame handling

# 🔧 Troubleshooting
# Camera not working: Check browser permissions or ensure no other app is using the camera.
# Slow performance: Use a smaller resolution or ensure your device isn't on power-saving mode.
# Model error: Ensure yolov8n.pt is in the same directory as app.py.

# 📄 License
# This project is licensed under the MIT License.
# Made with ❤️ using Streamlit and YOLOv8
# Last Updated: May 2026
