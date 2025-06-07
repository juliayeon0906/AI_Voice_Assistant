# 🎙️ AI Voice Assistant (GPT-Powered)

A simple, voice-activated AI assistant using Python and OpenAI's GPT model. Speak naturally, and the assistant listens, thinks, and talks back! Ideal for beginners exploring speech recognition, TTS, and conversational AI integration.

---

## 📌 Features

- 🎤 **Speech to Text** – Uses Google's Speech Recognition to convert voice input into text.
- 🤖 **Natural GPT Responses** – Sends input to OpenAI's GPT (gpt-4-mini) for human-like replies.
- 🔊 **Text to Speech** – Uses Google Text-to-Speech (`gTTS`) to speak responses out loud.
- 🛑 **Graceful Exit** – Just say “stop” and the assistant politely ends the session.

---

## 🗂 Project Structure
ai_voice_assistant/
├── ai_speaker.py # Main program: handles audio input/output
├── gpt.py # GPT response logic (OpenAI API integration)
├── README.md # Project documentation
└── requirements.txt # Python dependencies (optional but recommended)


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai_voice_assistant.git
cd ai_voice_assistant
```

### 2. Install Dependencies
Install the required Python packages using:
```
pip install -r requirements.txt
```
or
```
pip install openai speechrecognition gtts playsound
```

Note for macOS/Linux users: You may need to install portaudio and PyAudio:
```
brew install portaudio
pip install pyaudio
```


---

## 🌍 Language Support
- English
- French
- Korean


---


## 📜 License
This project is licensed under the MIT License © 2025 Julia Yeon