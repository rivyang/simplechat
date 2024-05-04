import { WebSocket } from 'isomorphic-ws';
import { config } from 'dotenv';

config();

const chatSocket = new WebSocket(process.env.WEBSOCKET_SERVER_URL);

const initializeChatSocketListeners = () => {
  chatSocket.on('open', () => {
    console.log('Connected to the chat server');
  });
  chatSocket.on('message', (message) => {
    displayChatMessage(message);
  });
  chatSocket.on('error', (error) => {
    console.error('WebSocket error: ', error);
  });
  chatSocket.on('close', () => {
    console.log('Disconnected from the chat server');
  });
};

const sendChatMessage = (message) => {
  chatSocket.send(message);
};

const displayChatMessage = (message) => {
  const chatMessagesContainer = document.getElementById('messages');
  const chatMessageElement = document.createElement('p');
  chatMessageElement.textContent = message;
  chatMessagesContainer.appendChild(chatMessageElement);
};

document.getElementById('send-message-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const messageInputField = document.getElementById('message-input');
  sendChatMessage(messageInputField.value);
  messageInputField.value = '';
});

initializeChatSocketListeners();