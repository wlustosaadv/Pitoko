const chatBox = document.getElementById('chat-box');
const input = document.getElementById('input');
const enviar = document.getElementById('enviar');

function addMessage(sender, text) {
  const div = document.createElement('div');
  div.classList.add(sender);
  div.textContent = `${sender === 'user' ? 'Você' : 'Pitoko'}: ${text}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function enviarMensagem() {
  const pergunta = input.value.trim();
  if (!pergunta) return;

  addMessage('user', pergunta);
  input.value = '';

  addMessage('bot', '⏳ Pitoko está pensando...');

  try {
    const res = await fetch('/api/pitoko', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ pergunta })
    });

    const data = await res.json();

    document.querySelectorAll('.bot:last-child')[0].textContent =
      `Pitoko: ${data.resposta || 'Ops! Algo deu errado 😿'}`;
  } catch (err) {
    addMessage('bot', '⚠️ Erro ao se conectar com o servidor.');
  }
}

enviar.addEventListener('click', enviarMensagem);
input.addEventListener('keydown', e => e.key === 'Enter' && enviarMensagem());
