import React, { useState } from 'react';
import ChatMessage from './ChatMessage';
import VoiceInput from './VoiceInput';

function ChatInterface() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [language, setLanguage] = useState('en');
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const sendMessage = async() => {
        if (input.trim() === '') return;

        const newMessage = { text: input, sender: 'user' };
        setMessages([...messages, newMessage]);
        setInput('');
        setIsLoading(true);
        setError(null);

        try {
            const response = await fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: input, language }),
            });
            if (!response.ok) {
                throw new Error('Failed to get response from server');
            }
            const data = await response.json();
            setMessages(prevMessages => [...prevMessages, { text: data.response, sender: 'bot' }]);
        } catch (error) {
            console.error('Error:', error);
            setError('An error occurred while processing your request. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    return ( <
            div className = "chat-interface" >
            <
            div className = "language-selector" >
            <
            select value = { language }
            onChange = {
                (e) => setLanguage(e.target.value) } >
            <
            option value = "en" > English < /option> <
            option value = "hi" > Hindi < /option> <
            /select> <
            /div> <
            div className = "chat-messages" > {
                messages.map((msg, index) => ( <
                    ChatMessage key = { index }
                    message = { msg }
                    />
                ))
            } {
                isLoading && < div className = "loading" > Processing... < /div>} {
                    error && < div className = "error" > { error } < /div>} <
                        /div> <
                        div className = "chat-input" >
                        <
                        input
                    type = "text"
                    value = { input }
                    onChange = {
                        (e) => setInput(e.target.value) }
                    onKeyPress = {
                        (e) => e.key === 'Enter' && sendMessage() }
                    placeholder = "Type your message here..."
                    disabled = { isLoading }
                    /> <
                    button onClick = { sendMessage }
                    disabled = { isLoading } > Send < /button> <
                        VoiceInput onSpeechResult = {
                            (result) => setInput(result) }
                    language = { language }
                    /> <
                    /div> <
                    /div>
                );
            }

            export default ChatInterface;