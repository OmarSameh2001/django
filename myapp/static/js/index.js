window.onload = function() {
    const messages = [
        "Welcome to our website!",
        "Hello! We're glad you're here.",
        "Hi there! Enjoy your visit.",
        "Welcome! Hope you have a great time."
    ];
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    alert(randomMessage);
};

