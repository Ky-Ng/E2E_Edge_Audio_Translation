from bluedot.btcomm import BluetoothClient
from bluedot.btcomm import BluetoothServer
from signal import pause


class BluetoothHandler():
    # Constructor for client
    def __init__(self, receivedCallbacks, sendingCallback, serverMacAddress=None) -> None:
        if serverMacAddress:
            self.c = BluetoothClient(serverMacAddress, self.on_data_received)
        else:
            self.c = BluetoothServer(self.on_data_received)
        self.receivedCallbacks = receivedCallbacks
        self.sendingCallback = sendingCallback

    # On data receipt, pass through all call backs
    def on_data_received(self, data):
        for callback in self.receivedCallbacks:
            callback(data)

    def send(self, msg:str) -> None:
        self.c.send(msg)

    # Infinite loop of sending to partner
    def start(self) -> None:
        while True:
            finalMsg = None # Should be overwritten
            for callback in self.sendingCallback:
                msg = callback(finalMsg)
                if msg:
                    finalMsg = msg
            self.send(finalMsg)
