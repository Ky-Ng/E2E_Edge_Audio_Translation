# import paho.mqtt.client as mqtt
# TOPIC_NAMESPACE = "e2e_translation"
# target_topic = f"{TOPIC_NAMESPACE}/e2e"


# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# client.connect(host="mqtt.eclipseprojects.io", port=1883, keepalive=60)
# client.loop_start()

# client.publish(target_topic, "testing 123")


# print("published message")
# while True:
#     pass

# client.loop_stop()
import sys
sys.path.append("./library")
from MQTTHandler import MQTTHandler



def test_received_callbacks(foo):
    print("receive callback")


def test_send_callbacks(foo):
    print("send callback")


mqtt = MQTTHandler([test_received_callbacks], [test_send_callbacks],
                   topic_namespace="e2e_translation", topic="e2e")
# mqtt = MQTTHandler(test_received_callbacks, test_send_callbacks)
mqtt.send("testing class")


while True:
    pass