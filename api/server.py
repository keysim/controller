from socketIO_client import SocketIO
with SocketIO('localhost', 8000) as socketIO:
    socketIO.emit('aaa')
    socketIO.wait(seconds=1)

#import bluetooth
#import time

bd_addr = "20:14:04:09:11:63"
port = 1
#sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
#sock.connect((bd_addr,port))

#while 1:
        #time.sleep(5)
        #sock.send("0")

#sock.close()
