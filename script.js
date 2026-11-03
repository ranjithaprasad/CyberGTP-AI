
const messages = document.getElementById("messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const newChatButton = document.getElementById("new-chat");

let conversation = [];

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.style.padding = "15px";
    message.style.margin = "12px auto";
    message.style.maxWidth = "800px";
    message.style.borderRadius = "10px";
    message.style.textAlign = "left";
    message.style.whiteSpace = "pre-wrap";
    message.style.background =
        sender === "user" ? "#1e3a5f" : "#1e293b";

    const label = document.createElement("strong");
    label.textContent = sender === "user" ? "You" : "CyberGTP AI";

    const content = document.createElement("p");
    content.textContent = text;
    content.style.marginTop = "8px";

    message.appendChild(label);
    message.appendChild(content);
    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;
    return content;
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text || sendButton.disabled) return;

    const welcome = messages.querySelector(".welcome");
    if (welcome) welcome.remove();

    addMessage(text, "user");
    conversation.push({ role: "user", content: text });

    userInput.value = "";
    sendButton.disabled = true;

    const replyElement = addMessage("Thinking...", "ai");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ messages: conversation })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "AI request failed.");
        }

        replyElement.textContent = data.reply;
        conversation.push({
            role: "assistant",
            content: data.reply
        });

    } catch (error) {
        replyElement.textContent = "Error: " + error.message;
        conversation.pop();
    } finally {
        sendButton.disabled = false;
        userInput.focus();
    }
}

sendButton.addEventListener("click", sendMessage);

userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") sendMessage();
});

newChatButton.addEventListener("click", function() {
    conversation = [];
    messages.innerHTML = `
        <div class="welcome">
            <h1>Welcome to CyberGPT AI</h1>
            <p>Your intelligent cybersecurity assistant.</p>
            <p>Ask me about cybersecurity, ethical hacking,
            networking and SOC analysis.</p>
        </div>
    `;
});
