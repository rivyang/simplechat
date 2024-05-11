import os
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

class ChatRoom:
    def __init__(self, room_name):
        if not isinstance(room_name, str):
            raise ValueError("room_name must be a string")
        self.room_name = room_name
        self.participants = []  # Changed from members for clarity
        self.chat_history = []  # Changed from messages for clarity

    def add_participant(self, participant):
        if not isinstance(participant, str):
            print("Participant name must be a string")
            return False
        try:
            if participant not in self.participants:
                self.participants.append(participant)
                return True
            return False
        except Exception as error:
            print(f"Unexpected error adding participant: {error}")
            return False

    def remove_participant(self, participant):
        if not isinstance(participant, str):
            print("Participant name must be a string")
            return False
        try:
            if participant in self.participants:
                self.participants.remove(participant)
                return True
            return False
        except Exception as error:
            print(f"Unexpected error removing participant: {error}")
            return False

    def send_chat_message(self, message):
        if not isinstance(message, str):
            print("Message must be a string")
            return False
        try:
            self.chat_history.append(message)
            print(f"Message in '{self.room_name}': {message}")
        except Exception as error:
            print(f"Unexpected error sending chat message: {error}")

    def display_chat_history(self):
        return self.chat_history

class ChatService:
    def __init__(self):
        self.chat_rooms = {}  # Renamed from rooms for explicit naming

    def create_chat_room(self, room_name):
        if not isinstance(room_name, str):
            print("Room name must be a string")
            return False
        try:
            if room_name not in self.chat_rooms:
                new_chat_room = ChatRoom(room_name)
                self.chat_rooms[room_name] = new_chat_room
                return True
            return False
        except Exception as error:
            print(f"Unexpected error creating chat room: {error}")
            return False

    def join_chat_room(self, room_name, participant):
        if not isinstance(room_name, str) or not isinstance(participant, str):
            print("Room name and participant name must be strings")
            return False
        try:
            if room_name in self.chat_rooms:
                return self.chat_rooms[room_name].add_participant(participant)
            return False
        except Exception as error:
            print(f"Unexpected error joining chat room: {error}")
            return False

    def leave_chat_room(self, room_name, participant):
        if not isinstance(room_name, str) or not isinstance(participant, str):
            print("Room name and participant name must be strings")
            return False
        try:
            if room_name in self.chat_rooms and participant in self.chat_rooms[room_name].participants:
                return self.chat_rooms[room_name].remove_participant(participant)
            return False
        except Exception as error:
            print(f"Unexpected error leaving chat room: {error}")
            return False

    def post_message(self, room_name, message):
        if not isinstance(room_name, str) or not isinstance(message, str):
            print("Room name and message must be strings")
            return False
        try:
            if room_name in self.chat_rooms:
                self.chat_rooms[room_name].send_chat_message(message)
                return True
            return False
        except Exception as error:
            print(f"Unexpected error posting message: {error}")
            return False

    def retrieve_chat_history(self, room_name):
        if not isinstance(room_name, str):
            print("Room name must be a string")
            return []
        try:
            if room_name in self.chat_rooms:
                return self.chat_rooms[room_name].display_chat_history()
            return []
        except Exception as error:
            print(f"Unexpected error retrieving chat history: {error}")
            return []