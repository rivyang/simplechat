import os
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.participants = []  # Changed from members for clarity
        self.chat_history = []  # Changed from messages for clarity

    def add_participant(self, participant):
        try:
            if participant not in self.participants:
                self.participants.append(participant)
                return True
            return False
        except Exception as error:
            print(f"Error adding participant: {error}")
            return False

    def remove_participant(self, participant):
        try:
            if participant in self.participants:
                self.participants.remove(participant)
                return True
            return False
        except Exception as error:
            print(f"Error removing participant: {error}")
            return False

    def send_chat_message(self, message):
        try:
            self.chat_history.append(message)
            print(f"Message in '{self.room_name}': {message}")
        except Exception as error:
            print(f"Error sending chat message: {error}")

    def display_chat_history(self):
        return self.chat_history

class ChatService:
    def __init__(self):
        self.chat_rooms = {}  # Renamed from rooms for explicit naming

    def create_chat_room(self, room_name):
        try:
            if room_name not in self.chat_rooms:
                new_chat_room = ChatRoom(room_name)
                self.chat_rooms[room_name] = new_chat_room
                return True
            return False
        except Exception as error:
            print(f"Error creating chat room: {error}")
            return False

    def join_chat_room(self, room_name, participant):
        try:
            if room_name in self.chat_rooms:
                return self.chat_rooms[room_name].add_participant(participant)
            return False
        except Exception as error:
            print(f"Error joining chat room: {error}")
            return False

    def leave_chat_room(self, room_name, participant):
        try:
            if room_name in self.chat_rooms and participant in self.chat_rooms[room_name].participants:
                return self.chat_rooms[room_name].remove_participant(participant)
            return False
        except Exception as error:
            print(f"Error leaving chat room: {error}")
            return False

    def post_message(self, room_name, message):
        try:
            if room_name in self.chat_rooms:
                self.chat_rooms[room_name].send_chat_message(message)
                return True
            return False
        except Exception as error:
            print(f"Error posting message: {error}")
            return False

    def retrieve_chat_history(self, room_name):
        try:
            if room_name in self.chat_rooms:
                return self.chat_rooms[room_name].display_chat_history()
            return []
        except Exception as error:
            print(f"Error retrieving chat history: {error}")
            return []