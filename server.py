import socketio
import eventlet
import eventlet.wsgi
import bluetooth
import time
from flask import Flask, render_template, send_from_directory

keyduino = "20:14:04:09:11:63"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sio = socketio.Server()
app = Flask(__name__, static_url_path='', template_folder='')
sock.connect((keyduino, port))


@app.route('/game/<path:path>')
def send_js(path):
    return send_from_directory('game', path)


@app.route('/')
def index():
    return render_template('game/index.html')


@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('1', namespace='/chat')
def message(sid, data):
    sock.send("1")
    print("message ", data)
    # sio.emit('reply', room=sid)


@sio.on('0', namespace='/chat')
def message(sid, data):
    sock.send("0")
    print("message ", data)
    # sio.emit('reply', room=sid)


@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)

sock.close()
print('Socket closed')
