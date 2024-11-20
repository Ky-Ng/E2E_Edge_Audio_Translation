from bluedot.btcomm import BluetoothClient
from signal import pause


class BluetoothHandler():
    MINDY_ADDR = "D8:3A:DD:B5:C2:EB"
    def __init__(self) -> None:
        self.c = BluetoothClient("D8:3A:DD:B5:C2:EB", self.on_data_received)

    def on_data_received(self, data):
        return data
    
    
    
    def send(self, msg:str) -> None:
        self.c.send(msg)


# msg = input("enter a message: ")
# while msg != '':

#     msg = input("enter a message: ")