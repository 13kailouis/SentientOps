const chatlog = document.getElementById('chatlog');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

function appendMessage(sender, text) {
  const div = document.createElement('div');
  div.classList.add('message');
  div.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatlog.appendChild(div);
  chatlog.scrollTop = chatlog.scrollHeight;
}

async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;
  appendMessage('You', text);
  userInput.value = '';

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text }),
    });
    const data = await response.json();
    if (data.reply) {
      appendMessage('Bot', data.reply);
    } else {
      appendMessage('Bot', data.error || 'No response');
    }
  } catch (err) {
    appendMessage('Bot', 'Error communicating with server');
  }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    sendMessage();
  }
});
