import json
import time
from sensor.dht11_sensor import DHT11Sensor
from mqtt.mqtt_client import MqttPublisher

class SensorManager:
    def __init__(self, config):
        self.sensor = DHT11Sensor(sensor_id=config["sensor_id"])
        self.publisher = MqttPublisher(
            config["broker"],
            config["port"],
            config["username"],
            config["password"],
            config["topic"]
        )

    def run(self):
        try:
            while True:
                data = self.sensor.read()
                if data:
                    message = json.dumps(data.to_dict())
                    print(f"[Data] {message}")
                    self.publisher.publish(message)
                time.sleep(3)
        except KeyboardInterrupt:
            print("\n[System] Interrupted by user. Shutting down...")
            self.shutdown()

    def shutdown(self):
        self.sensor.shutdown()
        self.publisher.shutdown()