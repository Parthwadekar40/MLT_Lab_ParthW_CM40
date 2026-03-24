# 🌐 Browser-Based Machine Learning with TensorFlow.js

This repository is a comprehensive series of projects focused on the integration of **Machine Learning** directly into the web browser and Node.js environments. From fundamental regression models to advanced real-time computer vision, this collection explores the power of **TensorFlow.js**.

---

## 📌 Project Overview

This series of projects is designed to provide a comprehensive understanding of the Machine Learning lifecycle within the JavaScript ecosystem, moving from theoretical foundations to real-world deployment.

* **Foundation:** Grasping the core mechanics of Tensors, hardware acceleration via WebGL, and the foundational principles of TensorFlow.js.
* **Neural Architectures:** Engineering and analyzing diverse models, including Sequential layers, Convolutional Neural Networks (CNNs) for vision, and Recurrent Neural Networks (RNNs) for sequence data.
* **Edge Intelligence:** Deploying industry-standard pre-trained models like MobileNet and PoseNet for real-time, browser-based webcam analysis.
* **Optimization & Adaptation:** Leveraging Transfer Learning to repurpose powerful architectures for custom datasets and specialized real-world applications.

---
---

## 📂 Project Roadmap & Practical Labs

| No. | Project Title | Description | Status |
| :--- | :--- | :--- | :--- |
| 00 | [Hello TensorFlow.js](./HelloTensorFlowJS) | Environment setup and basic Tensor operations. | ✅ Complete |
| 01 | [Linear Regression](./Linear-Regression) | Training a simple regression model on synthetic data. | ✅ Complete |
| 02 | [Digit Recognition](./Digit-Recognition) | MNIST handwritten digit classification using CNNs. | ✅ Complete |
| 03 | [Sentiment Analysis](./Text-Sentiment-Analysis) | Natural Language Processing (NLP) to classify text. | ✅ Complete |
| 04 | [Image Classification](./Image-classification) | Using MobileNet for instant browser-based recognition. | ✅ Complete |
| 05 | [Real-time Object Detection](./Web-cam) | Webcam-based detection and frame-by-frame analysis. | ✅ Complete |
| 06 | [Pose Detection](./Pose-Detection) | Human body pose estimation using PoseNet. | ✅ Complete |
| 07 | [Model Deployment](./Model-in-Browser) | Saving, reloading, and serving trained models locally. | ✅ Complete |
| 08 | Transfer Learning | Customizing MobileNet for specific image categories. | ⏳ Coming Soon |

---

## 🛠️ Tech Stack
* **Engine:** TensorFlow.js
* **Language:** JavaScript (ES6+)
* **Environments:** Google Chrome (WebGL), Node.js
* **Models:** MobileNet, PoseNet, MNIST, Custom Sequential Layers

---

## 🏃 Quick Start Guide

To run any of the projects in this repository locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Parthwadekar40/MLT_Lab_ParthW_CM40.git](https://github.com/Parthwadekar40/MLT_Lab_ParthW_CM40.git)
    ```

2.  **Serve the Web Projects:**
    Since many projects use the Webcam API or load local files, you need a local server. You can use `Live Server` in VS Code or `http-server` via npm:
    ```bash
    # Install http-server globally if you haven't
    npm install -g http-server
    
    # Run the server
    http-server .
    ```

3.  **Access:**
    Open your browser and navigate to `http://localhost:8080`.

---
