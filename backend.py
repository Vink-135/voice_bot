# backend.py
import speech_recognition as sr
from gtts import gTTS
import os
import google.generativeai as genai

genai.configure(api_key="YOUR API KEY")

def record_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening... Speak now.")
        audio = r.listen(source, timeout=5, phrase_time_limit=100)
    return r.recognize_google(audio)

def get_gemini_reply(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    return response.text

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename
