import paho.mqtt.client as mqtt
TOPIC_NAMESPACE = "e2e_translation"
target_topic = f"{TOPIC_NAMESPACE}/e2e"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connecting to {target_topic}")
    client.subscribe(target_topic)

@client.topic_callback(target_topic)
def on_message_led(client, userdata, msg):
    print(f"Received: {str(msg.payload, 'utf-8')}")

client.on_connect = on_connect
client.connect(host="mqtt.eclipseprojects.io", port=1883, keepalive=60)
client.loop_start()

while True:
    pass

client.loop_stop()
