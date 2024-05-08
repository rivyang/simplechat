from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key!')
socketio = SocketIO(app, cors_allowed_origins="*")

active_rooms = {}  # Key: room_name, Value: dict with a list of participants

@app.route('/create_room', methods=['POST'])
def create_chat_room():
    room_name = request.json.get('room_name')
    if room_name in active_rooms:
        return jsonify({'status': 'error', 'message': f'Room "{room_name}" already exists!'}), 400
    active_rooms[room_name] = {'participants': []}
    return jsonify({'status': 'success', 'message': f'Room "{room_name}" created successfully!'}), 201

@app.route('/delete_room', methods=['POST'])
def delete_chat_room():
    room_name = request.json.get('room_name')
    if room_name not in active_rooms:
        return jsonify({'status': 'error', 'message': f'Room "{room_name}" does not exist!'}), 404
    del active_rooms[room_name]
    return jsonify({'status': 'success', 'message': f'Room "{room_name}" deleted successfully!'}), 200

@socketio.on('join_room')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    if room not in active_rooms:
        active_rooms[room] = {'participants': []}  # Auto-create room if doesn't exist upon join
    active_rooms[room]['participants'].append(username)
    emit('room_status', {'msg': f'{username} has joined the room.'}, room=room)

@socketio.on('leave_room')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    # Safety check to avoid crashing if room somehow doesn't exist
    if room in active_rooms and username in active_rooms[room]['participants']:
        active_rooms[room]['participants'].remove(username)
        emit('room_status', {'msg': f'{username} has left the room.'}, room=room)

@socketio.on('send_message')
def on_message(data):
    emit('message_received', data, room=data['room'])

if __name__ == '__main__':
    socket_port = os.getenv('SOCKET_PORT', '5000')
    socketio.run(app, debug=True, host='0.0.0.0', port=int(socket_port))