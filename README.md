# 🎙️ Gemini Voice Assistant — Real-Time VoiceBot using Google Gemini & Streamlit

> A powerful real-time conversational VoiceBot that listens to your voice 🎤, understands your query 🤖, and responds back with audio 🔊 — just like ChatGPT meets Google Assistant!

---


## 📌 Features

✅ Realtime Microphone Input  
✅ Google Gemini API for responses  
✅ Google Speech Recognition  
✅ gTTS (Text-to-Speech) for reply audio  
✅ Conversational UI (chat bubbles)  
✅ Works entirely in-browser  
✅ Streamlit UI (modern, responsive)

---

## 🧠 Tech Stack

| Area                | Tool/Lib Used           |
|---------------------|-------------------------|
| Voice Recognition   | `SpeechRecognition`, `pyaudio`  
| Text Generation     | `Google Gemini API`  
| Text-to-Speech      | `gTTS`  
| Web App UI          | `Streamlit`  
| Audio Playback      | `Streamlit Audio`, `tempfile`  

---

## 📂 Project Structure

```bash
Gemini-VoiceBot/
│
├── voice_ui.py                 # Streamlit UI
├── backend.py             # All backend functions
├── requirements.txt       # All dependencies
└── README.md              # You’re reading this file!

```

---

## ⚙️ How It Works

1. **Click the button** → activates your mic  
2. 🎤 **Voice is captured** via SpeechRecognition  
3. 🤖 **Query is sent to Gemini** using Gemini Pro API  
4. 💬 **Gemini replies back** → both shown as chat + converted to voice  
5. 🔊 **Voice output is auto-played** using `gTTS`

---





