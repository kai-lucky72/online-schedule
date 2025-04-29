import paho.mqtt.client as mqtt
import serial
import time

# Setup MQTT
broker = "localhost"
topic = "light/schedule"

# Setup serial connection with Arduino (adjust port accordingly)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Callback function when message is received from MQTT
def on_message(client, userdata, message):
    schedule = message.payload.decode('utf-8')
    on_time, off_time = schedule.split(',')
    
    print(f"Received schedule: ON at {on_time}, OFF at {off_time}")
    
    # Send command to Arduino (1 for ON, 0 for OFF)
    # Adjust timing logic as necessary
    arduino.write(b'1')  # '1' for ON (you can add timing logic)
    time.sleep(10)  # Adjust time based on your schedule
    arduino.write(b'0')  # '0' for OFF

# Setup MQTT client
client = mqtt.Client()
client.on_message = on_message

client.connect(broker)
client.subscribe(topic)

# Loop forever
client.loop_forever()
