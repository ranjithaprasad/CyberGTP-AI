
const messages = document.getElementById("messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const newChatButton = document.getElementById("new-chat");

// Display messages
function addMessage(text, sender) {
    const message = document.createElement("div");

    message.style.padding = "15px";
    message.style.margin = "12px auto";
    message.style.maxWidth = "800px";
    message.style.borderRadius = "10px";
    message.style.textAlign = "left";
    message.style.whiteSpace = "pre-wrap";

    if (sender === "user") {
        message.style.background = "#1e3a5f";
    } else {
        message.style.background = "#1e293b";
    }

    const label = document.createElement("strong");
    label.textContent = sender === "user"
        ? "You"
        : "CyberGTP AI";

    const content = document.createElement("p");
    content.textContent = text;
    content.style.marginTop = "8px";

    message.appendChild(label);
    message.appendChild(content);
    messages.appendChild(message);
}

// Send message
function sendMessage() {
    const text = userInput.value.trim();

    if (text === "") {
        return;
    }

    const welcome = messages.querySelector(".welcome");
    if (welcome) {
        welcome.remove();
    }

    addMessage(text, "user");

    userInput.value = "";

    addMessage(
        "Hello! I'm CyberGTP AI. AI integration is coming soon. I will help you with cybersecurity questions!",
        "ai"
    );
}

// Button click
sendButton.addEventListener("click", sendMessage);

// Enter key
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// New chat
newChatButton.addEventListener("click", function() {
    messages.innerHTML = `
        <div class="welcome">
            <h1>Welcome to CyberGTP AI</h1>
            <p>Your intelligent cybersecurity assistant.</p>
            <p>Ask me about cybersecurity, ethical hacking,
            networking and SOC analysis.</p>
        </div>
    `;
});
