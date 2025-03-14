MQTT-Based Light Control
Project Overview
This project is a simple web-based application that allows a user to switch a light ON/OFF using MQTT. The app simulates an IoT device (ESP8266) using Python, which listens for MQTT messages and prints the light status.

Features
✅ Web interface with "Turn ON" and "Turn OFF" buttons
✅ Uses MQTT.js to publish messages via WebSockets
✅ Simulated IoT device in Python that subscribes to MQTT messages
✅ Prints light status ("ON" or "OFF") in real time

Project Structure
graphql
Copy
Edit
📂 MQTT-Light-Control  
 ├── 📄 index.html          # Web interface (MQTT.js frontend)  
 ├── 📄 light_simulation.py # Simulated IoT device (Python)  
 ├── 📄 README.md           # Project documentation  
 ├── 📄 styles.css           # Html styling
Setup & Installation

1️⃣ Run the Python MQTT Listener
Make sure you have Python installed. Install the required package:
pip install paho-mqtt

Run the Python script:
python light_simulation.py

2️⃣ Open the Web Interface
Simply open index.html in your browser and click the buttons to send MQTT messages.

How It Works
The web app connects to an MQTT broker using MQTT.js.
Clicking "Turn ON" or "Turn OFF" publishes "ON" or "OFF" to the MQTT topic /student_group/light_control.
The Python script subscribes to the same topic and prints:
💡 Light is TURNED ON if it receives "ON".
💡 Light is TURNED OFF if it receives "OFF".

Author
👨‍💻 Dieudonne
📅 March 14, 2025