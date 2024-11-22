from bluedot.btcomm import BluetoothClient
from signal import pause

def data_received(data):
    print(data)

c = BluetoothClient("D8:3A:DD:B5:C2:EB", data_received)
c.send("helloworld")

pause()