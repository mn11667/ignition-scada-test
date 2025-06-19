# sensor_simulator.py
import random
import time

def generate_sensor_data():
    while True:
        temperature = round(random.uniform(20.0, 40.0), 2)
        pressure = round(random.uniform(1.0, 2.0), 2)
        print(f"Temperature: {temperature}°C | Pressure: {pressure} bar")
        time.sleep(2)

if __name__ == "__main__":
    generate_sensor_data()
    