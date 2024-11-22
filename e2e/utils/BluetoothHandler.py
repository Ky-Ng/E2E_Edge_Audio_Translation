from bluedot.btcomm import BluetoothClient
from bluedot.btcomm import BluetoothServer
from signal import pause


class BluetoothHandler():
    # MINDY_ADDR = "D8:3A:DD:B5:C2:EB"
    # Constructor for server
    def __init__(self, receivedCallbacks, sendingCallback) -> None:
        self.c = BluetoothServer(self.on_data_received)
        self.receivedCallbacks = receivedCallbacks
        self.sendingCallback = sendingCallback

    # Constructor for client
    def __init__(self, receivedCallbacks, sendingCallback, serverMacAddress) -> None:
        self.c = BluetoothClient(serverMacAddress, self.on_data_received)
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
            self.send(self.sendingCallback())
