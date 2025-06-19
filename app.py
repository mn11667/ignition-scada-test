from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/sensor")
def get_sensor_data():
    return jsonify({
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "pressure": round(random.uniform(1.0, 2.0), 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
    


    