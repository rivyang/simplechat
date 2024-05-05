import os
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.messages = []

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            return True
        return False

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            return True
        return False

    def broadcast_message(self, message):
        self.messages.append(message)
        print(f"Broadcasting in '{self.name}': {message}")

    def list_messages(self):
        return self.messages

class ChatManager:
    def __init__(self):
        self.rooms = {}

    def create_room(self, room_name):
        if room_name not in self.rooms:
            new_room = ChatRoom(room_name)
            self.rooms[room_name] = new_room
            return True
        return False

    def join_room(self, room_name, member):
        if room_name in self.rooms:
            return self.rooms[room_name].add_member(member)
        return False

    def leave_room(self, room_name, member):
        if room_name in self.rooms and member in self.rooms[room_name].members:
            return self.rooms[room_name].remove_member(member)
        return False

    def send_message(self, room_name, message):
        if room_name in self.rooms:
            self.rooms[room_name].broadcast_message(message)
            return True
        return False

    def get_messages(self, room_name):
        if room_name in self.rooms:
            return self.rooms[room_name].list_messages()
        return []