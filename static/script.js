document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");

    // Debugging: Check if elements exist
    if (!chatForm) console.error("Error: #chat-form is missing in the HTML.");
    if (!userInput) console.error("Error: #user-input is missing in the HTML.");
    if (!chatMessages) console.error("Error: #chat-messages is missing in the HTML.");

    if (!chatForm || !userInput || !chatMessages) return;

    chatForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        const userMessage = userInput.value.trim();
        if (userMessage === "") return;

        // Append user message to chat
        const userMessageElement = document.createElement("div");
        userMessageElement.classList.add("user-message");
        userMessageElement.textContent = userMessage;
        chatMessages.appendChild(userMessageElement);

        // Show loading indicator
        const loadingElement = document.createElement("div");
        loadingElement.classList.add("loading");
        loadingElement.textContent = "Thinking...";
        chatMessages.appendChild(loadingElement);

        userInput.value = "";

        try {
            const response = await fetch("http://0.0.0.0:8000/query", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: userMessage }),
            });

            if (!response.ok) {
                throw new Error("Server error, please try again.");
            }

            const data = await response.json();
            chatMessages.removeChild(loadingElement);

            const botMessageElement = document.createElement("div");
            botMessageElement.classList.add("bot-message");
            botMessageElement.textContent = data.response;
            chatMessages.appendChild(botMessageElement);
        } catch (error) {
            chatMessages.removeChild(loadingElement);
            console.error("Error:", error);
            alert("Error communicating with the server.");
        }
    });
});
