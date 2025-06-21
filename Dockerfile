FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Install paho-mqtt
RUN pip install --no-cache-dir paho-mqtt

CMD ["python", "app.py"]
