import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def message(sid, data):
    sio.send(data)

@sio.event
def disconnect(sid):
    
    data = {
        "id":1, 
        "status":False,
        "temp":"_",
        "con_speed":"_",
        "cpu":"_",
        "camera":False,
        "ir":False
    }
    sio.send(data)
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    