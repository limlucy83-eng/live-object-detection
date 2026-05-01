```

---

## 📦 Dependencies

| Package | Version | Purpose |
| :--- | :--- | :--- |
| **streamlit** | ≥1.28.0 | Web application framework |
| **streamlit-webrtc** | ≥0.47.0 | WebRTC integration for video streaming |
| **ultralytics** | ≥8.0.0 | YOLOv8 object detection |
| **opencv-python** | ≥4.8.0 | Image processing |
| **av** | ≥10.0.0 | Video frame handling (PyAV) |
| **numpy** | ≥1.24.0 | Numerical operations |

---

## ⚙️ Configuration

### Model Parameters
*   **Confidence Threshold**: 0.5 (adjustable in `app.py`)
*   **Model**: YOLOv8 Nano (lightweight, fast inference)
*   **Tracking**: Enabled with persistent tracking

### Video Settings
*   **Resolution**: 1280x720 (ideal)
*   **Audio**: Disabled
*   **Processing**: Asynchronous

---

## 🎯 Supported Object Classes
YOLOv8n is trained on the COCO dataset and can detect 80 object classes including:
*   **People**
*   **Vehicles** (cars, buses, trucks)
*   **Animals** (cats, dogs, birds)
*   **Household items** (bottles, chairs, laptops)
*   **Sports equipment** (balls, bats)

---

## 🔧 Troubleshooting

*   **Camera not working**: 
    *   Ensure you've granted camera permissions to your browser.
    *   Check if another application is using the camera.
    *   Try using HTTPS if accessing remotely.
*   **Slow performance**:
    *   Close unnecessary browser tabs.
    *   Reduce video resolution in browser settings.
    *   Ensure GPU acceleration is enabled (if available).
*   **Model not loading**:
    *   Verify `yolov8n.pt` is in the project directory.
    *   Check internet connection for initial download.

---

## 🤝 Contributing

1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

*   [Streamlit](https://streamlit.io/) - For the amazing web framework
*   [Ultralytics](https://ultralytics.com/) - For YOLOv8
*   [OpenCV](https://opencv.org/) - For computerHere is the complete documentation formatted into a single Markdown block for easy copying and pasting.
```markdown
# 🎥 Live Object Detection & Tracing

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-8.0+-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A real-time object detection and tracking web application built with Streamlit, YOLOv8, and WebRTC. This application provides live video analysis directly from your webcam with instant object detection and counting capabilities.

---

## ✨ Features

*   🎯 **Real-time Detection**: Process video frames in real-time with minimal latency.
*   📊 **Object Counting**: Automatic counting of detected objects with on-screen display.
*   🎥 **WebRTC Integration**: Direct webcam access through browser using WebRTC.
*   🤖 **YOLOv8 Nano**: Lightweight yet powerful object detection model.
*   📱 **Responsive UI**: Clean, modern interface built with Streamlit.
*   🔄 **Object Tracking**: Persistent tracking of objects across frames.
*   💚 **Visual Feedback**: Bounding boxes and labels overlaid on video feed.

---

## 📋 Prerequisites

*   Python 3.8 or higher
*   Webcam
*   Modern web browser (Chrome, Firefox, Edge, or Safari)
*   `pip` package manager

---

## 🚀 Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd live_objective
    ```

2.  **Create a virtual environment (Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the YOLOv8 model**
    > The model will automatically download on the first run, or you can place `yolov8n.pt` in the root directory manually.

---

## 📁 Project Structure

```text
live_objective/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── yolov8n.pt         # YOLOv8 model weights
├── utils/              # Helper functions
└── README.md           # Documentation
```

---

## 🎮 Usage

1.  **Run the application**
    ```bash
    streamlit run app.py
    ```

2.  **Access the application**
    *   The app will open automatically in your default browser.
    *   Or navigate to `http://localhost:8501`.

3.  **Grant camera permissions**
    *   When prompted, allow browser access to your webcam.
    *   Ensure good lighting for optimal detection.

4.  **View detection results**
    *   Objects will be detected and tracked in real-time.
    *   Object count is displayed in the top-left corner.
    *   Bounding boxes show detected objects with class labels.

---

## 💻 Code Overview

### Main Components

**Model Loading**
```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
```

**Video Frame Processing**
```python
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Perform detection
    results = model.track(img, persist=True, conf=0.5)
    
    # Annotate frame
    annotated_frame = results[0].plot()
    
    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")
```

**WebRTC Streamer Configuration**
```python
webrtc_streamer(
    key="object-detection",
    video_frame_callback=video_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)
```

---

## 📦 Dependencies

| Package | Version | Purpose |
| :--- | :--- | :--- |
| **streamlit** | ≥1.28.0 | Web application framework |
| **streamlit-webrtc** | ≥0.47.0 | WebRTC integration for video streaming |
| **ultralytics** | ≥8.0.0 | YOLOv8 object detection |
| **opencv-python** | ≥4.8.0 | Image processing |
| **av** | ≥10.0.0 | Video frame handling (PyAV) |
| **numpy** | ≥1.24.0 | Numerical operations |

---

## ⚙️ Configuration

### Model Parameters
*   **Confidence Threshold**: 0.5 (adjustable in `app.py`)
*   **Model**: YOLOv8 Nano (lightweight, fast inference)
*   **Tracking**: Enabled with persistent tracking

### Video Settings
*   **Resolution**: 1280x720 (ideal)
*   **Audio**: Disabled
*   **Processing**: Asynchronous

---

## 🎯 Supported Object Classes
YOLOv8n is trained on the COCO dataset and can detect 80 object classes including:
*   **People**
*   **Vehicles** (cars, buses, trucks)
*   **Animals** (cats, dogs, birds)
*   **Household items** (bottles, chairs, laptops)
*   **Sports equipment** (balls, bats)

---

## 🔧 Troubleshooting

*   **Camera not working**: 
    *   Ensure you've granted camera permissions to your browser.
    *   Check if another application is using the camera.
    *   Try using HTTPS if accessing remotely.
*   **Slow performance**:
    *   Close unnecessary browser tabs.
    *   Reduce video resolution in browser settings.
    *   Ensure GPU acceleration is enabled (if available).
*   **Model not loading**:
    *   Verify `yolov8n.pt` is in the project directory.
    *   Check internet connection for initial download.

---

## 🤝 Contributing

1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

*   [Streamlit](https://streamlit.io/) - For the amazing web framework
*   [Ultralytics](https://ultralytics.com/) - For YOLOv8
*   [OpenCV](https://opencv.org/) - For computer vision capabilities

**Made with ❤️ using Streamlit and YOLOv8**  
*Last Updated: May 2026*
```
