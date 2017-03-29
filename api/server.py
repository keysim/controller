from . import socket_io as io

class Server(io.Server):
    def on_connect(self, client):
        print(client, 'connected')
        self.broadcast(str(client) + ' connected')
        print('there are now', len(self.clients), 'clients')

    def on_message(self, client, message):
        print(client, 'sent', message)
        client.send(message)

    def on_disconnect(self, client):
        print(client, 'disconnected')
        self.broadcast(str(client) + ' disconnected')
        print('there are now', len(self.clients), 'clients')

Server().listen(5000)


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
