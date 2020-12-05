from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS,cross_origin
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

socketio = SocketIO(app,cors_allowed_origins="*")
CORS(app,resources={r"/*":{'origins': "http://localhost:3000"}})

colours = ['red','green','yellow','blue']
def emit_colour():
    i = 0
    print ('threading')
    while i < 4:
        #socketio.emit('response',{'data':'yeet'})
        socketio.emit('response',{'colour':colours[i]})
        time.sleep(5)
        i += 1

@app.route('/')
def hello():
    return ('hello')

@socketio.on('connect',namespace='/')
def connect():
    print ('connected')
    #socketio.emit('response',{'data':'yeet'})
    t = threading.Thread(target=emit_colour)
    t.start()

if __name__ == '__main__':
    socketio.run(app,debug=True,host='0.0.0.0',port=5555)
