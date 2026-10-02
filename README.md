# OpenCV Programs

> A collection of Computer Vision programs built with Python & OpenCV

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green.svg)

##  Overview

This repository contains a set of beginner-to-intermediate computer vision programs built using OpenCV and Python. Each script demonstrates a specific concept such as image filtering, edge detection, face detection, object tracking, and more. The goal of this repo is to practice and showcase core computer vision techniques with clean, well-documented code.

##  Features

- Real-time webcam video capture and processing
- Face, eye and smile detection using Haar cascades
- Image filtering (blur, edge detection, thresholding)
- Color detection and object tracking
- Simple, well-commented and beginner-friendly code

##  Requirements

- Python 3.10 or higher
- opencv-python
- numpy
- A working webcam (for live-video scripts)

##  Installation

```bash
# Clone the repository
git clone https://github.com/your-username/opencv-mini-projects.git
cd opencv-mini-projects

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage

```python
import cv2

# Load the image
image = cv2.imread('input.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the result
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

##  Folder Structure

```
opencv-mini-projects/
├── cv1.py
├── cvv2.py
├── cv3.py upto 20
├── images/
│   └── sample.jpg
├── requirements.txt
└── README.md
```

##  Contributing

Contributions are welcome! Feel free to fork this repository, open issues, or submit pull requests.

##  License

This project is licensed under the **MIT** license.

##  Author

**Vivek Singh Chauhan** · [GitHub](https://github.com/Vivekk936)
