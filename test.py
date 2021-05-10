from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)



async_mode = None



@app.route('/')
def homepage():
   
    
    return render_template('test.html', async_mode=socketio.async_mode)




if __name__ == '__main__':
    portis = os.environ.get('PORT')
    if(portis == None):
        portis = 5000
    else:
        portis = int(portis)
    print(portis)
    socketio.run(app, host= "0.0.0.0", port= portis, debug=False)