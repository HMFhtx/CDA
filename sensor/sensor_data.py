class SensorData:
    def __init__(self, sensor_id, temperature, humidity, timestamp):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "sensor_id": self.sensor_id,
            "temperature": f"{self.temperature:.1f}C",
            "humidity": f"{self.humidity:.1f}%",
            "timestamp": self.timestamp
        }

    def __str__(self):
        return str(self.to_dict())