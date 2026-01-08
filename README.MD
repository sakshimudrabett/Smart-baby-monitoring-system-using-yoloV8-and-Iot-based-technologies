# Smart Baby Monitoring System using YOLOv8 and IoT Technologies

An **AI- and IoT-based Smart Baby Monitoring System** designed to assist parents in monitoring their baby’s safety using real-time visual intelligence and sensor-based alerts.  
The project combines **computer vision (YOLOv8)**, **IoT (ESP32)**, and a **Flask-based web dashboard** in a modular and fault-tolerant architecture.

---

## 📌 Problem Statement

Continuous manual monitoring of infants is difficult for parents.  
Traditional baby monitors provide only video or audio streaming without intelligence, alerts, or environmental awareness.

This project aims to enhance baby monitoring by integrating:
- AI-based visual monitoring
- IoT-based environmental sensing
- Real-time alerts
- A secure web dashboard for parents

---

## 🏗️ System Architecture

The project follows a **layered architecture**:

1. **IoT Edge Layer**
   - ESP32 with sensors (Temperature, Sound, Motion)
   - Immediate alerts via buzzer and SMS
   - Cloud logging using ThingSpeak

2. **AI Intelligence Layer**
   - YOLOv8 object detection model (`best.pt`)
   - Real-time baby detection from live camera feed

3. **Application Layer**
   - Flask-based web dashboard
   - Parent login & authentication
   - Live monitoring interface
   - Activity log and system status

This separation ensures **low latency**, **reliability**, and **fault tolerance**.

---

## ⚙️ Technologies Used

### 🧠 Artificial Intelligence
- YOLOv8 (Object Detection)
- PyTorch
- OpenCV

### 🌐 Web & Backend
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- HTML, CSS (Dark-themed UI)

### 📡 IoT & Embedded
- ESP32
- DHT22 (Temperature Sensor)
- Sound Sensor
- PIR Motion Sensor
- Buzzer

### ☁️ Cloud Services
- Twilio (SMS Alerts)
- ThingSpeak (Sensor Data Logging)

### 🗄️ Database
- SQLite (User authentication data)

---

## 🚀 Features

- Secure parent login & signup
- Live video monitoring with AI detection
- Camera status indicator (LIVE / OFFLINE)
- Activity log for transparency
- IoT-based alerts (Temperature, Sound, Motion)
- SMS notifications for critical events
- Cloud-based sensor data logging
- Modular and scalable design

---

## 📁 Project Structure

Smart-baby-monitoring-system/
│
├── backend/
│ ├── app.py
│ ├── yolo_camera.py
│ └── auth.py
│
├── templates/
│ ├── login.html
│ ├── signup.html
│ └── dashboard.html
│
├── static/
│ └── style.css
│
├── models/
│ └── model.pt
│
├── iot/
│ └── esp32_baby_monitor.txt
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 🔐 Authentication & Database

- Parent credentials are stored using **SQLite**
- Flask-Login manages user sessions
- SQLite was chosen due to:
  - Lightweight and serverless nature
  - Ease of setup
  - Suitability for academic projects

---

## 📡 IoT Module (ESP32)

The IoT module:
- Reads temperature, sound, and motion data
- Triggers local alerts (buzzer)
- Sends SMS alerts using Twilio
- Uploads sensor data to ThingSpeak

> The IoT code is included as a **reference document**, as the firmware was developed and tested using **Arduino IDE**.

---

## 🔒 Security Considerations

- Edge-based alerts ensure reliability even if the dashboard is unavailable
- Alert cooldown mechanisms prevent notification flooding
- Sensitive credentials are handled carefully during deployment

---

## 📈 Future Enhancements

- Real-time sensor integration with Flask dashboard
- REST API communication between ESP32 and server
- Graphical visualization of sensor data
- Mobile application support
- Cloud deployment
- AI-based anomaly detection

---

## 🎓 Academic Relevance

This project demonstrates:
- Practical use of AI in real-time systems
- Integration of IoT with cloud services
- Secure web application development
- Modular system design inspired by real-world engineering practices

---

## 👥 Team Members

- Sakshi Mudrabett  
- Team Member 2  
- Team Member 3  

---

## 📜 Conclusion

This project showcases how **AI and IoT technologies** can be effectively combined to build a **reliable, intelligent, and user-friendly baby monitoring system**, emphasizing safety, real-time alerts, and system transparency.

---
