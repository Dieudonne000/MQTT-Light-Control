import paho.mqtt.client as mqtt

# MQTT settings
BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

# Callback when a message is received
def on_message(client, userdata, msg):
    command = msg.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

# Setup MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)

# Subscribe to the topic
client.subscribe(TOPIC)
print("Listening for MQTT messages...")

client.loop_forever()
