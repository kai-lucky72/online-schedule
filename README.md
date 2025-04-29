# Web-Based Light Scheduler (IoT Simulation)

A lightweight IoT dashboard to schedule light ON/OFF times via a web interface, using WebSockets and MQTT to simulate a smart home device. This project demonstrates real-time communication between a web client, a WebSocket server, an MQTT broker, and a microcontroller (Arduino UNO).

## 📌 Overview

This system allows a user to schedule when a light turns ON or OFF through a browser interface. The schedule is sent over WebSockets to a Python server, which publishes it to an MQTT topic. A Python subscriber script listens for MQTT messages and sends corresponding commands (`'1'` for ON, `'0'` for OFF) to an Arduino via serial communication. The Arduino then controls a relay to switch the light.

---

## ⚙️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript (WebSocket)
- **Backend**:
  - WebSocket Server: Python with `websockets`
  - MQTT Publisher/Subscriber: `mosquitto_pub`, `mosquitto_sub`, `paho-mqtt`
  - Serial Communication: `pyserial`
- **MQTT Broker**: Mosquitto
- **Microcontroller**: Arduino UNO

---

## 📁 Project Structure


---

## 🚀 How to Run the Project

### 🔧 Prerequisites

- Python 3.7+
- Arduino UNO + USB Cable
- Mosquitto MQTT Broker installed and running on `localhost`
- Python packages:
  ```bash
  pip install websockets paho-mqtt pyserial
