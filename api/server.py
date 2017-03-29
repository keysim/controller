from socketIO_client import SocketIO
with SocketIO('192.168.1.100', 8000) as socketIO:
    socketIO.emit('aaa', {"LOL":"OK"})
    socketIO.wait(seconds=1)