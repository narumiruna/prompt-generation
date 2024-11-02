document.getElementById("chat-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    const messageInput = document.getElementById("message");
    const historyInput = document.getElementById("history");
    const messagesList = document.getElementById("messages");
    const loadingIndicator = document.getElementById("loading");

    // Show loading indicator
    loadingIndicator.style.display = "inline";

    const formData = new FormData(this);
    formData.append("message", messageInput.value);
    formData.append("history", historyInput.value || "[]");

    try {
        const response = await fetch(this.action, {
            method: this.method,
            body: formData
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const result = await response.json();
        historyInput.value = JSON.stringify(result.history);

        // Update chat messages
        messagesList.innerHTML = "";
        result.history.forEach(msg => {
            const li = document.createElement("li");
            li.innerHTML = marked.parse(msg.content);
            li.classList.add(msg.role);
            messagesList.appendChild(li);
        });

        // Save to localStorage
        localStorage.setItem("chatHistory", JSON.stringify(result.history));

        // Clear message input
        messageInput.value = "";

        // Scroll to the latest message
        scrollToBottom();
    } catch (error) {
        console.error("Error generating response:", error);
        alert("An error occurred while generating the response. Please try again.");
    } finally {
        // Hide loading indicator
        loadingIndicator.style.display = "none";
    }
});

function scrollToBottom() {
    const chatBox = document.getElementById("chat-box");
    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById("message").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("chat-form").submit();
    }
});
