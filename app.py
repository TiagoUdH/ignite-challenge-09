from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

socketio = SocketIO(app)

users_amount = 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    message = f'Usuário {session['user_number']}: {msg}'
    emit('message', message, broadcast=True)
    
@socketio.on('connect')
def handle_connect():
    user_id = str(uuid.uuid4())
    session['user_id'] = user_id
    
    global users_amount
    users_amount += 1
    
    session['user_number'] = users_amount
    
    emit('message', f'Usuário {users_amount} está online', broadcast=True)
    
@socketio.on('disconnect')
def handle_connect():
    emit('message', f'Usuário {session['user_number']} está offline', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
