// Подключаемся к WebSocket серверу
let socket = new WebSocket("ws://web/ws/chat/");

// Когда соединение установлено
socket.onopen = function(event) {
    console.log("WebSocket соединение установлено.");
};

// Когда приходит сообщение
// socket.onmessage = function(event) {
//     let data = JSON.parse(event.data);
//     let chatMessages = document.querySelector('.chat-messages');
//     let newMessage = document.createElement('div');
//     newMessage.classList.add('chat-message');
//     newMessage.textContent = data.message;
    
//     chatMessages.appendChild(newMessage);
//     chatMessages.scrollTop = chatMessages.scrollHeight;
// };

// Когда соединение закрывается
socket.onclose = function(event) {
    console.log("WebSocket соединение закрыто.");
};

// Когда происходит ошибка
socket.onerror = function(error) {
    console.error("WebSocket ошибка:", error);
};

// Обработка отправки сообщения
// document.getElementById('send-btn').addEventListener('click', function() {
//     let chatInput = document.getElementById('chat-input');
//     let message = chatInput.value;
    
//     if (message.trim() !== "") {
//         // Отправляем сообщение через WebSocket
//         socket.send(JSON.stringify({ 'message': message }));
        
//         chatInput.value = ""; // Очищаем поле ввода
//     }
// });

// Отправка сообщения при нажатии Enter
// document.getElementById('chat-input').addEventListener('keypress', function(e) {
//     if (e.key === 'Enter') {
//         document.getElementById('send-btn').click();
//     }
// });