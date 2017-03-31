# import socketio
# import threading
# import eventlet
# import eventlet.wsgi
# import bluetooth
# from flask import Flask, render_template, send_from_directory
#
# print("Starting BLE...")
#
# keyduino = "20:14:04:09:11:63"
# port = 1
# size = 1024
# room = ""
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
# print("Starting socketIO and flask...")
#
# sio = socketio.Server()
# app = Flask(__name__, static_url_path='', template_folder='')
#
# sock.connect((keyduino, port))
#
#
# def bt_read():
#     global room
#     buf = ""
#     good = ""
#     while 1:
#         data = sock.recv(size).decode('utf-8')
#         if data:
#             if data.endswith(';'):
#                 buf += data
#                 good = buf
#                 sio.emit('input', good, room=room)
#                 print(good)
#                 print(room)
#                 buf = ""
#             else:
#                 buf += data
#
# thr = threading.Thread(target=bt_read, args=(), kwargs={})
# thr.start()
#
#
# @app.route('/game/lib/<path:path>')
# def send_js(path):
#     return send_from_directory('game/lib/', path)
#
#
# @app.route('/')
# def index():
#     return render_template('game/index.html')
#
#
# @sio.on('connect', namespace='/controller')
# def connect(sid, environ):
#     global room
#     room = sid
#     print("connect ", sid)
#
#
# @sio.on('1', namespace='/controller')
# def message(sid, data):
#     sock.send("1")
#     print("ON ", data)
#     # sio.emit('reply', room=sid)
#
#
# @sio.on('0', namespace='/controller')
# def message(sid, data):
#     sock.send("0")
#     print("OFF ", data)
#     sio.emit('input', "TEST", room=sid)
#
#
# @sio.on('BLE', namespace='/controller')
# def connect_ble(sid, data):
#     sock.connect((keyduino, port))
#
#
# @sio.on('disconnect', namespace='/controller')
# def disconnect(sid):
#     print('disconnect ', sid)
#
# if __name__ == '__main__':
#     app = socketio.Middleware(sio, app)
#     eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)
#
# sock.close()
# print('END OF SCRIPT')

from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import threading
import bluetooth

app = Flask(__name__, template_folder='game')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

print("Starting BLE...")

keyduino = "20:14:04:09:11:63"
port = 1
size = 1024
room = ""
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

print("Starting socketIO and flask...")

sock.connect((keyduino, port))


def bt_read():
    global room
    buf = ""
    good = ""
    while 1:
        data = sock.recv(size).decode('utf-8')
        if data:
            if data.endswith(';'):
                buf += data
                good = buf
                with app.test_request_context('/'):
                    emit('input', good)
                print(good)
                print(room)
                buf = ""
            else:
                buf += data

thr = threading.Thread(target=bt_read, args=(), kwargs={})
thr.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game/lib/<path:path>')
def send_js(path):
    return send_from_directory('game/lib/', path)


@socketio.on('1')
def test_message(message):
    emit('input', {'data': 'got it!'})


@socketio.on('connect')
def connect():
    print("connected !")

if __name__ == '__main__':
    socketio.run(app, '0.0.0.0')
