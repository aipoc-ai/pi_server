import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')

for i in range(10):
	sio.send("data")
sio.wait()