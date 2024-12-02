import paho.mqtt.client as mqtt
TOPIC_NAMESPACE = "e2e_translation"
target_topic = f"{TOPIC_NAMESPACE}/e2e"


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(host="mqtt.eclipseprojects.io", port=1883, keepalive=60)
client.loop_start()

client.publish(target_topic, "testing 123")


print("published message")
while True:
    pass

client.loop_stop()
