from config import CONFIG
from sensor_manager import SensorManager

if __name__ == "__main__":
    manager = SensorManager(CONFIG)
    manager.run()