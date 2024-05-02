import { WebSocket } from 'isomorphic-ws';
import { config } from 'dotenv';
config();
const ws = new WebSocket(process.env.WEBSOCKET_SERVER_URL);
const initWebSocketListeners = () => {
  ws.on('open', () => {
    console.log('Connected to the chat server');
  });
  ws.on('message', (data) => {
    displayMessage(data);
  });
  ws.on('error', (error) => {
    console.error('WebSocket error: ', error);
  });
  ws.on('close', () => {
    console.log('Disconnected from the chat server');
  });
};
const sendMessage = (message) => {
  ws.send(message);
};
const displayMessage = (message) => {
  const messagesContainer = document.getElementById('messages');
  const messageElement = document.createElement('p');
  messageElement.textContent = message;
  messagesContainer.appendChild(messageElement);
};
document.getElementById('send-message-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const messageInput = document.getElementById('message-input');
  sendMessage(messageInput.value);
  messageInput.value = '';
});
initWebSocketListeners();