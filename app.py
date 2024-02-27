from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)
    
@socketio.on('connect')
def handle_connect():
    emit('message', 'Usuário está online', broadcast=True)
    
@socketio.on('disconnect')
def handle_connect():
    emit('message', 'Usuário está offline', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
