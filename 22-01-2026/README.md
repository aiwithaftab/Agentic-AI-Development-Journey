# Computer Vision & Structure from Motion (SfM) Learning Journey

This repository contains my learning notes and practical implementations for the **Computer Vision Lab (Associate Degree Program)**. The focus of today's session was on image processing fundamentals and 3D reconstruction using Structure from Motion.

## 🚀 Key Topics Covered

### 1. Fundamental Image Operations
* **Preprocessing:** Grayscale conversion, Gaussian Blurring, and Thresholding.
* **Edge Detection:** Implementing the Canny Edge Detection algorithm.
* **Contour Analysis:** Finding and drawing shapes using `cv2.findContours`.

### 2. Structure from Motion (SfM)
SfM is a photogrammetric technique for estimating 3D structures from 2D image sequences.

#### **The SfM Pipeline implemented:**
1. **Feature Detection:** Using **ORB (Oriented FAST and Rotated BRIEF)** to find keypoints.
2. **Feature Matching:** Matching descriptors using **Brute-Force Matcher** with Hamming distance.
3. **Motion Estimation:** Calculating the **Essential Matrix (E)** using RANSAC for outlier removal.
4. **Pose Recovery:** Extracting Rotation ($R$) and Translation ($t$) from the Essential Matrix.
5. **Triangulation:** Converting 2D matched points into **3D spatial coordinates**.

---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Library:** OpenCV (`cv2`), NumPy

---

## 💻 Code Snippets & Logic

### Feature Matching with ORB
```python
orb = cv2.ORB_create(5000)
kp1, des1 = orb.detectAndCompute(gray1, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
