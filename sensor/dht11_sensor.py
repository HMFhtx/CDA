import board
import adafruit_dht
import time
from sensor.sensor_data import SensorData

class DHT11Sensor:
    def __init__(self, pin=board.D4, sensor_id="Sensor_02"):
        self.sensor_id = sensor_id
        self.device = adafruit_dht.DHT11(pin, use_pulseio=False)

    def read(self):
        try:
            temp = self.device.temperature
            hum = self.device.humidity
            if temp is not None and hum is not None:
                timestamp = time.strftime("%H:%M")
                return SensorData(self.sensor_id, temp, hum, timestamp)
        except RuntimeError as e:
            print(f"[Sensor] Read error: {e}")
        return None

    def shutdown(self):
        self.device.exit()