import React, { useState } from 'react';

function VoiceInput({ onSpeechResult, language }) {
    const [isListening, setIsListening] = useState(false);

    const startListening = () => {
        if ('webkitSpeechRecognition' in window) {
            const recognition = new window.webkitSpeechRecognition();
            recognition.lang = language === 'hi' ? 'hi-IN' : 'en-US';
            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                onSpeechResult(transcript);
            };
            recognition.onend = () => setIsListening(false);
            recognition.start();
            setIsListening(true);
        } else {
            alert('Speech recognition is not supported in your browser.');
        }
    };

    return ( <
        button onClick = { startListening }
        disabled = { isListening } > { isListening ? 'Listening...' : 'Start Voice Input' } <
        /button>
    );
}

export default VoiceInput;