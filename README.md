
A modern, full-stack application that detects people in images or video frames and estimates crowd density in real-time. This project bridges a high-performance **YOLOv8** backend with a sleek **React** frontend.

---

## 📖 Overview
The **Crowd Density Estimator** provides an end-to-end solution for monitoring occupancy. By leveraging the speed of YOLOv8-nano, the system can process visual data on both CPU and GPU, providing instant density metrics and visual feedback through a clean, interactive dashboard.

<img width="1045" height="636" alt="g3" src="https://github.com/user-attachments/assets/03641950-8add-4a36-8ea9-edd1e24b0fdb" />
<img width="1045" height="636" alt="g2" src="https://github.com/user-attachments/assets/09487fa6-ffe3-4200-82db-e47d4f5448df" />
<img width="1045" height="636" alt="g1" src="https://github.com/user-attachments/assets/9ee4d9d4-9401-495f-8ebb-0ff6363f540a" />


## ✨ Features
* **Real-time Detection:** High-speed inference using `yolov8n.pt`.
* **Density Analytics:** Automatically computes density levels based on person counts.
* **Modern UI:** Built with **React + Vite + Tailwind CSS**, featuring a custom `DensityIndicator` component.
* **Rapid Development:** Instant Hot Module Replacement (HMR) and a unified startup script.
* **One-Command Run:** Simplified workflow to launch both services simultaneously.

---

## 🏗️ Architecture

### Backend (Python)
- **`detector.py`**: The core engine; loads YOLOv8 and handles person detection logic.
- **`main.py`**: FastAPI/Flask API endpoints to bridge the model with the web.
- **`yolov8n.pt`**: Pre-trained weights optimized for speed.

### Frontend (React)
- **`DensityIndicator.jsx`**: A visual component that changes state based on crowd levels.
- **Tailwind CSS**: Used for a responsive, mobile-friendly design.
- **Vite**: Ensures a lightning-fast frontend build process.

---

## 🛠️ Getting Started

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**

### 1. Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt

