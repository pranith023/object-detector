import streamlit as st
import cv2
from ultralytics import YOLO
import time

# ✅ Page title
st.title("📹 Real-Time Object Detection with YOLOv8")
st.write("Enter your IP camera stream URL below (from IP Camera Lite):")

# ✅ Input for IP Camera URL
ip_url = st.text_input("Camera Stream URL", "http://10.110.192.2:8081/video")

# ✅ Confidence threshold
conf_threshold = st.slider("Confidence Threshold", 0.25, 0.9, 0.5)

# ✅ Model selection
model_choice = st.selectbox("Choose YOLOv8 Model", ["yolov8n.pt (fast)", "yolov8m.pt (balanced)", "yolov8l.pt (accurate)"])
model_path = model_choice.split()[0]
model = YOLO(model_path)

# ✅ Buttons
start = st.button("Start Detection")
stop = st.button("Stop Detection")

# ✅ Placeholder for video
stframe = st.empty()

# ✅ Start detection when button is clicked
if start:
    cap = cv2.VideoCapture(ip_url)

    if not cap.isOpened():
        st.error("❌ Unable to connect to IP camera. Please check the URL.")
    else:
        st.success("✅ Connected to camera!")
        prev_time = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to grab frame.")
                break

            # ✅ YOLO detection
            results = model(frame, conf=conf_threshold)
            annotated_frame = results[0].plot()

            # ✅ FPS calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time
            cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # ✅ Show frame in Streamlit
            stframe.image(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB), channels="RGB")

            # ✅ Check stop button
            if stop:
                st.warning("🛑 Detection Stopped.")
                break

        cap.release()
