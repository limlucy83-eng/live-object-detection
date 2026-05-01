🎥 Live Object Detection & Tracing
A real-time object detection and tracking web application built with Streamlit, YOLOv8, and WebRTC. This application provides live video analysis directly from your webcam with instant object detection and counting capabilities.
✨ Features
🎯 Real-time Detection: Process video frames in real-time with minimal latency
📊 Object Counting: Automatic counting of detected objects with on-screen display
🎥 WebRTC Integration: Direct webcam access through browser using WebRTC
🤖 YOLOv8 Nano: Lightweight yet powerful object detection model
📱 Responsive UI: Clean, modern interface built with Streamlit
🔄 Object Tracking: Persistent tracking of objects across frames
💚 Visual Feedback: Bounding boxes and labels overlaid on video feed
📋 Prerequisites
Python 3.8 or higher
Webcam
Modern web browser (Chrome, Firefox, Edge, or Safari)
pip package manager
🚀 Installation
Clone the repository
bash
12
Create a virtual environment (recommended)
bash
1234567
Install dependencies
bash
1
Download the YOLOv8 model (if not already present)
bash
123
📁 Project Structure
123456
🎮 Usage
Run the application
bash
1
Access the application
The app will open automatically in your default browser
Or navigate to http://localhost:8501
Grant camera permissions
When prompted, allow browser access to your webcam
Ensure good lighting for optimal detection
View detection results
Objects will be detected and tracked in real-time
Object count is displayed in the top-left corner
Bounding boxes show detected objects with class labels
💻 Code Overview
Main Components
Model Loading
python
12345
Video Frame Processing
python
12345678910111213141516171819202122
WebRTC Streamer Configuration
python
1234567
📦 Dependencies
Package
Version
Purpose
streamlit
≥1.28.0
Web application framework
streamlit-webrtc
≥0.47.0
WebRTC integration for video streaming
ultralytics
≥8.0.0
YOLOv8 object detection
opencv-python
≥4.8.0
Image processing
av
≥10.0.0
Video frame handling (PyAV)
numpy
≥1.24.0
Numerical operations
⚙️ Configuration
Model Parameters
Confidence Threshold: 0.5 (adjustable in app.py)
Model: YOLOv8 Nano (lightweight, fast inference)
Tracking: Enabled with persistent tracking
Video Settings
Resolution: 1280x720 (ideal)
Audio: Disabled
Processing: Asynchronous
🎯 Supported Object Classes
YOLOv8n is trained on COCO dataset and can detect 80 object classes including:
People
Vehicles (cars, buses, trucks)
Animals
Household items
Sports equipment
And many more...
🔧 Troubleshooting
Camera not working
Ensure you've granted camera permissions to your browser
Check if another application is using the camera
Try using HTTPS if accessing remotely
Slow performance
Close unnecessary browser tabs
Reduce video resolution in browser settings
Ensure GPU acceleration is enabled (if available)
Model not loading
Verify yolov8n.pt is in the project directory
Check internet connection for initial download
Ensure sufficient disk space
🚀 Performance Optimization
For better performance:
Use GPU acceleration (CUDA-enabled PyTorch)
Reduce video resolution if needed
Adjust confidence threshold
Use a more powerful YOLO model if accuracy is prioritized over speed
Customization
Change Detection Model
python
1234
Adjust Confidence Threshold
python
123456
🤝 Contributing
Contributions are welcome! Please follow these steps:
Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments
Streamlit - For the amazing web framework
Ultralytics - For YOLOv8
OpenCV - For computer vision capabilities
PyAV - For video frame handling
📞 Support
For issues and questions:
Open an issue on GitHub
Check existing documentation
Review troubleshooting section
🔗 Links
Streamlit Documentation
YOLOv8 Documentation
WebRTC Guide
Made with ❤️ using Streamlit and YOLOv8
Last Updated: May 2026
