# Sparse vs. Dense Optical Flow Analysis

This repository contains a Python-based comparative study of Optical Flow techniques used in Computer Vision. The project implements and compares **Lucas-Kanade (Sparse)** and **Farneback (Dense)** algorithms to track motion in a juggling sequence.

## 📌 Project Objective
The goal of this project is to analyze the trade-offs between sparse and dense motion estimation. Specifically, the implementation is optimized to isolate the movement of fast-moving juggling balls while ignoring background static features and noise.

## 🛠️ Requirements
* Python 3.x
* OpenCV (`cv2`)
* NumPy
* Matplotlib

## 🔬 Algorithms Implemented

### 1. Lucas-Kanade (Sparse Optical Flow)
Tracks the motion of a select set of "interesting" pixels (features).
* **Optimization:** Initialized tracking points using **Hough Circle Transform** to ensure motion vectors are locked onto the juggling balls rather than background textures (like door handles or text).
* **Visualization:** Represented by red points (current position) and green vectors (motion history).



### 2. Farneback (Dense Optical Flow)
Computes a motion vector for every single pixel in the frame to create a complete flow field.
* **Optimization:** Implemented a **magnitude threshold** to zero out sub-pixel noise, ensuring the static background remains black while the motion of the balls and arms is clearly highlighted.
* **Visualization:** Uses **HSV Color Encoding**. 
    * **Hue:** Represents the direction of motion.
    * **Value:** Represents the speed of motion.



## 📊 Comparison Summary

| Metric | Lucas-Kanade (Sparse) | Farneback (Dense) |
| :--- | :--- | :--- |
| **Tracking Level** | Specific keypoints (Features) | Global (Per-pixel) |
| **Speed** | Extremely Fast (Real-time) | Computationally Intensive |
| **Output Type** | Discrete Vectors | Continuous Flow Map |
| **Robustness** | High for tracked features | Sensitive to global noise |
| **Best Use Case** | Robot Navigation / Object Tracking | Action Recognition / Video Analysis |

## 📈 Results
The final implementation successfully isolates the juggling balls. The Sparse method provides clean trajectory data for the balls, while the Dense method visualizes the "motion cloud" created by the juggler's arms and the balls' arcs, proving the complementary nature of these two techniques.

---
*Developed as part of a Computer Vision University Assignment.*
