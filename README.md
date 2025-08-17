# Real-Time Object Detection with YOLOv8

A Streamlit-based web application for real-time object detection using YOLOv8 models. This application connects to IP camera streams and performs live object detection with customizable confidence thresholds and model selection.

## 🚀 Features

- **Real-time object detection** from IP camera streams
- **Multiple YOLOv8 model options**:
  - YOLOv8n (Nano) - Fastest inference speed
  - YOLOv8m (Medium) - Balanced speed and accuracy
  - YOLOv8l (Large) - Highest accuracy
- **Adjustable confidence threshold** (0.25 - 0.9)
- **Live FPS display** for performance monitoring
- **Start/Stop controls** for detection management
- **Responsive web interface** built with Streamlit



## 📋 Requirements

- Python 3.7+
- OpenCV (cv2)
- Streamlit
- Ultralytics YOLO
- IP camera with accessible stream URL

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd real-time-yolo-detection
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install streamlit opencv-python ultralytics
   ```

3. **Ensure YOLO models are available**:
   - The application expects YOLOv8 model files in the project directory
   - Models will be automatically downloaded on first use if not present

## 🎯 Usage

### 1. Start the Application
```bash
streamlit run app.py
```

### 2. Configure Detection Settings
- **Camera Stream URL**: Enter your IP camera's video stream URL
  - Default: `http://10.100.192.2:8081/video`
  - Format: `http://<camera-ip>:<port>/video`
- **Confidence Threshold**: Adjust the slider (0.25 - 0.9)
  - Lower values = More detections (may include false positives)
  - Higher values = Fewer, more confident detections
- **Model Selection**: Choose between speed vs accuracy trade-offs

### 3. Start Detection
- Click **"Start Detection"** to begin real-time object detection
- View live results with bounding boxes and class labels
- Monitor FPS in the top-left corner of the video feed
- Click **"Stop Detection"** to pause the stream

## 📱 IP Camera Setup

### For IP Camera Lite App:
1. Install "IP Camera Lite" on your mobile device
2. Connect your phone to the same network as your computer
3. Open the app and note the displayed URL (usually `http://<phone-ip>:8081/video`)
4. Enter this URL in the application

### For Other IP Cameras:
- Check your camera's documentation for the RTSP or HTTP stream URL
- Common formats:
  - `http://<ip-address>:<port>/video`


## 🔧 Troubleshooting

### Common Issues:

**❌ "Unable to connect to IP camera"**
- Verify the camera URL is correct
- Ensure camera and computer are on the same network
- Check firewall settings
- Try accessing the URL in a web browser first

**⚠️ "Failed to grab frame"**
- Check camera permissions
- Verify the stream is active
- Try refreshing the camera app

**Slow performance**
- Use YOLOv8n for faster processing
- Lower the video resolution if possible
- Check network connection quality

## 📊 Model Comparison

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|--------|----------|----------|
| YOLOv8n | 6.2 MB | ⚡ Fastest | Good | Real-time applications |
| YOLOv8m | 21.2 MB | ⚡ Fast | Very Good | Balanced performance |
| YOLOv8l | 43.0 MB | Moderate | Excellent | High accuracy needs |

## 🏗️ Project Structure

```
real-time-yolo-detection/
├── app.py                 # Main Streamlit application
├── yolov8n.pt            # YOLOv8 Nano model
├── yolov8m.pt            # YOLOv8 Medium model
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## 🔍 Technical Details

- **Framework**: Streamlit for web interface
- **Detection**: Ultralytics YOLOv8 for object detection
- **Video Processing**: OpenCV for camera capture and frame processing
- **Performance**: Real-time processing with FPS monitoring
- **Supported Classes**: All COCO dataset classes (80 object types)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

For issues or questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Contact the maintainers
