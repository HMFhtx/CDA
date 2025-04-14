import paho.mqtt.client as mqtt
import ssl
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class MqttPublisher:
    def __init__(self, broker, port, username, password, topic):
        self.topic = topic
        self.client = mqtt.Client(client_id="pythonPublisher", protocol=mqtt.MQTTv5)
        self.client.username_pw_set(username, password)
        self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
        self.client.tls_insecure_set(True)
        self.client.on_connect = self.on_connect
        self.client.connect(broker, port, keepalive=60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print("[MQTT] Connected" if rc == 0 else f"[MQTT] Failed: {rc}")

    def publish(self, message):
        self.client.publish(self.topic, message, qos=1)

    def shutdown(self):
        self.client.loop_stop()
        self.client.disconnect()