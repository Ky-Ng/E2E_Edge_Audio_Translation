import sys
sys.path.append("./library")

from MQTTHandler import MQTTHandler


def test_received_callbacks(foo):
    print("receive callback")


def test_send_callbacks(foo):
    print("send callback")


mqtt = MQTTHandler([test_received_callbacks], [test_send_callbacks],
                   topic_namespace="e2e_translation", topic="e2e")

mqtt.send("testing class")


while True:
    pass
