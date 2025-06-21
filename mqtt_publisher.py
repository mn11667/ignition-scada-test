import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.loop_start()

while True:
    temperature = round(random.uniform(20.0, 40.0), 2)
    pressure = round(random.uniform(1.0, 2.0), 2)

    client.publish("sensors/data/temperature", str(temperature))
    client.publish("sensors/data/pressure", str(pressure))

    print(f"Published → temperature: {temperature}, pressure: {pressure}")
    time.sleep(2)
    