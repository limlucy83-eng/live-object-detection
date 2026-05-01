import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

st.set_page_config(page_title="AI Object Detector", layout="wide")
st.title("🎥 Live Object Detection & Tracing")
st.markdown("""
    **Status:** Active 🟢  
    **Instructions:** Allow access to your camera.
""")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    results = model.track(
        img,
        persist=True,
        conf=0.5,
        verbose=False
    )

    if results[0].boxes is not None:
        count = len(results[0].boxes)
    else:
        count = 0

    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame, 
        f"Detected Objects: {count}", 
        (20, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1.2, 
        (0, 255, 0), 
        3
    )

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

webrtc_streamer(
    key="object-detection",
    video_frame_callback=video_frame_callback,
    async_processing=True,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    },
    media_stream_constraints={
        "video": {
            "width": {"ideal": 1280},
            "height": {"ideal": 720}
        },
        "audio": False
    },
)

st.sidebar.header("System Info")
st.sidebar.write("Model: YOLOv8 Nano")
st.sidebar.write("Framework: Streamlit & PyAV")
st.sidebar.markdown("---")
st.sidebar.info("Tip: Make sure the surroundings are well-lit for more accurate detection.")