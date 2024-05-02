from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret!')
socketio = SocketIO(app, cors_allowed_origins="*")

chat_rooms = {}

@app.route('/create_room', methods=['POST'])
def create_room():
    data = request.json
    room_name = data.get('room_name')
    if room_name in chat_rooms:
        return jsonify({'status': 'error', 'message': f'Room {room_name} already exists!'}), 400
    chat_rooms[room_name] = {'participants': []}
    return jsonify({'status': 'success', 'message': f'Room {room_name} created successfully!'}), 201

@app.route('/delete_room', methods=['POST'])
def delete_room():
    data = request.json
    room_name = data.get('room_name')
    if room_name not in chat_rooms:
        return jsonify({'status': 'error', 'message': f'Room {room_name} does not exist!'}), 404
    del chat_rooms[room_name]
    return jsonify({'status': 'success', 'message': f'Room {room_name} deleted successfully!'}), 200

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    chat_rooms[room]['participants'].append(username)
    emit('status', {'msg': f'{username} has entered the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    chat_rooms[room]['participants'].remove(username)
    emit('status', {'msg': f'{username} has left the room.'}, room=room)

@socketio.on('send_message')
def handle_send_message_event(data):
    emit('receive_message', data, room=data['room'])

if __name__ == '__main__':
    socket_port = os.getenv('SOCKET_PORT', 5000)
    socketio.run(app, debug=True, host='0.0.0.0', port=socket_port)