import socketio
from time import sleep
from random import randint
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://127.0.0.1:5000')


for i in range(10):
    data = {
        "id":1, 
        "status":True,
        "temp":str(randint(1,100)),
        "con_speed":str(randint(1,100)),
        "cpu":str(randint(1,100)),
        "camera":True,
        "ir":True
    }
    sio.send(data)
    sleep(1)