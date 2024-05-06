import { WebSocket } from 'isomorphic-ws';
import { config } from 'dotenv';

config();

const chatSocket = initializeWebSocket(process.env.WEBSOCKET_SERVER_URL);

function initializeWebSocket(serverUrl) {
  const socket = new WebSocket(serverUrl);
  socket.on('open', handleOpenConnection);
  socket.on('message', handleMessageReceived);
  socket.on('error', handleErrorEvent);
  socket.on('close', handleCloseConnection);
  return socket;
}

function handleOpenConnection() {
  console.log('Connected to the chat server');
}

function handleMessageReceived(message) {
  displayChatMessage(message);
}

function handleErrorEvent(error) {
  console.error('WebSocket error: ', error);
}

function handleCloseConnection() {
  console.log('Disconnected from the chat server');
}

function sendChatMessage(message) {
  chatSocket.send(message);
}

function displayChatMessage(message) {
  const chatMessagesContainer = document.getElementById('messages');
  const chatMessageElement = document.createElement('p');
  chatMessageElement.textContent = message;
  chatMessagesContainer.appendChild(chatMessageElement);
}

function setupMessageSending() {
  const sendMessageForm = document.getElementById('send-message-form');
  sendMessageForm.addEventListener('submit', handleSendMessage);
}

function handleSendMessage(event) {
  event.preventDefault();
  const messageInputField = document.getElementById('message-input');
  const message = messageInputField.value;
  sendChatMessage(message);
  messageInputField.value = '';
}

function initializeApplication() {
  setupMessageSending();
}

initializeApplication();