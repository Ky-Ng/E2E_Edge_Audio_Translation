import paho.mqtt.client as mqtt
import os
import json


class MQTTHandler():
    TOPIC_NAMESPACE = "o_of_ng_e2e_translation"
    DEFAULT_TOPIC = "e2e_default_topic"

    MQTT_SERVER_URL = "mqtt.eclipseprojects.io"
    MQTT_SERVER_PORT = 1883
    MQTT_KEEP_ALIVE_TIME_IN_SEC = 60

    # Constructor for client
    def __init__(self, receivedCallbacks, sendingCallback, topic=DEFAULT_TOPIC) -> None:
        """
        Create an MQTT client which is both a subscriber and publisher to the 
        "MQTTHandler.TOPIC_NAMESPACE/topic" topic.

        In order to avoid echoing a message we send out, we will drop any received MQTT messages
        with our process ID.

        We assume that process IDs are highly unlikely to have a collision;
         for a 32 bit PID, collision probability is:
            1 - [p(no collision on first address) * p (no collision on second address) ... p (no collision on nth address)]
            1 - p(no collision) = 1 - (1 * 2^32-1/2^32)
        """
        self.uid = os.getpid()
        self.topic = f"{MQTTHandler.TOPIC_NAMESPACE}/{topic}"
        self.receivedCallbacks = receivedCallbacks
        self.sendingCallback = sendingCallback

        # Create MQTT Client and start communication with Server
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(
            host=MQTTHandler.MQTT_SERVER_URL,
            port=MQTTHandler.MQTT_SERVER_PORT,
            keepalive=MQTTHandler.MQTT_KEEP_ALIVE_TIME_IN_SEC
        )
        self.client.loop_start()
        
        # Subscribe and create receive callbacks
        self.client.on_connect = self.on_connect
        # TODO figure out with jonathan on the implementation of on_data_received
        # self.client.on_message = self.on_data_received 
    
    def __del__(self):
        # Cleanup MQTT client
        self.client.loop_stop()

    # On data receipt, pass through all call backs
    def on_data_received(self, data):
        for callback in self.receivedCallbacks:
            callback(data)

    def send(self, msg: str) -> None:
        # Prepare message
        message = {
            "uid": self.uid,
            "msg": msg
        }

        # Convert to JSON
        msg_str = json.dumps(message)

        # Send over MQTT
        self.client.publish(self.topic, msg_str)

    # Infinite loop of sending to partner
    def start(self) -> None:
        while True:
            finalMsg = None  # Should be overwritten
            for callback in self.sendingCallback:
                msg = callback(finalMsg)
                if msg:
                    finalMsg = msg
            self.send(finalMsg)
    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        self.client.subscribe(self.topic)
    
