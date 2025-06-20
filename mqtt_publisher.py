import paho.mqtt.client as mqtt
import time
import random
import json

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temperature = round(random.uniform(20.0, 40.0), 2)
    pressure = round(random.uniform(1.0, 2.0), 2)
    data = {
        "temperature": temperature,
        "pressure": pressure
    }
    client.publish("sensors/data", json.dumps(data))
    print("Published:", data)
    time.sleep(2)
