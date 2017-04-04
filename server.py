from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
# import threading
import bluetooth

async_mode = None

app = Flask(__name__, template_folder='game')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

print("Starting BLE...")

keyduino = "20:14:04:09:11:63"
port = 1
size = 1024
room = ""
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
thread = None

print("Starting socketIO and flask...")

sock.connect((keyduino, port))
sock.settimeout(0.05)


def background_thread():
    print("Background thread started...")
    while True:
        socketio.sleep(0.05)
        try:
            data = sock.recv(size).decode('utf-8')
            socketio.emit('input', {'data': data})
            print("data sent !")
        except:
            data = ""


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/game/lib/<path:path>')
def send_js(path):
    return send_from_directory('game/lib/', path)


@socketio.on('1')
def test_message(message):
    print("ON PRESSED")
    emit('input', {'data': 'got it!'})


@socketio.on('connect')
def connect():
    print("connected !")


@socketio.on('input', namespace='/test')
def send_input():
    print("penis !")


if thread is None:
    thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, '0.0.0.0')
