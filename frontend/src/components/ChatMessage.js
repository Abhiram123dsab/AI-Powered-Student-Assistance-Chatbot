import React from 'react';

function ChatMessage({ message }) {
    return ( <
        div className = { `chat-message ${message.sender}` } >
        <
        p > { message.text } < /p> <
        /div>
    );
}

export default ChatMessage;