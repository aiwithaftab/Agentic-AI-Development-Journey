# Real-Time Intelligent Object Detection & Statistical Logging
### Powered by YOLOv8 & OpenCV

## 📌 Project Overview
This project implements a robust real-time object detection pipeline using **YOLOv8**. Beyond simple detection, the system includes an **Automated Statistical Logging** engine that captures detection data for analytics, making it ideal for industrial monitoring, retail foot-traffic analysis, or security.

## 🚀 Key Features
* **Optimized Inference:** Fine-tuned confidence and IoU thresholds to balance precision and recall.
* **Live Statistical Logging:** Automatically exports detection events (Object Class, Timestamp, Confidence) to a CSV/Log file.
* **Performance Scaling:** Implemented frame-skipping and resolution scaling to maintain high FPS on local CPU/GPU hardware.
* **Visual Feedback:** Real-time annotated video stream with dynamic count overlays.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Model:** Ultralytics YOLOv8 (Nano/Small variants)
* **Vision:** OpenCV, Supervision
* **Data:** Pandas, NumPy

## 📊 Optimization Log
To achieve production-grade results, I implemented the following optimizations:

| Feature | Implementation | Result |
| :--- | :--- | :--- |
| **False Positive Reduction** | Increased `conf` to 0.5 & adjusted `iou` | Removed background noise/ghosting |
| **Inference Speed** | Frame Skipping (Process every $n^{th}$ frame) | 30% increase in FPS on local CPU |
| **Data Integrity** | Pandas-based buffering | Prevented I/O lag during CSV writes |

