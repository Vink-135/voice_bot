# app.py
import streamlit as st
from backend import record_and_transcribe, get_gemini_reply, text_to_speech
import os

st.set_page_config(page_title="🧠 Vink -VoiceBot", layout="centered")

# --- CSS Styling ---
st.markdown("""
    <style>
    .user-bubble {
        background-color: #007BFF;
        color: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        text-align: left;
        max-width: 80%;
        margin-left: auto;
        border: 1px solid #0056b3;
        box-shadow: 0px 1px 5px rgba(0,0,0,0.1);
    }
    .bot-bubble {
        background-color: #007BFF;
        color: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        text-align: left;
        max-width: 80%;
        margin-right: auto;
        border: 1px solid #0056b3;
        box-shadow: 0px 1px 5px rgba(0,0,0,0.1);
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎙️ Vink Voice Assistant</div>', unsafe_allow_html=True)
st.markdown("Speak something, and Vink-Voice-Bot will listen, think, and speak back to you!")

# --- Main Button ---
if st.button("🎤 Talk to Vink-VoiceBot"):
    with st.spinner("Listening..."):
        try:
            user_input = record_and_transcribe()
            st.markdown(f'<div class="user-bubble">🧑‍💬 <b>You said:</b><br>{user_input}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"🎤 Could not transcribe your voice: {e}")
            st.stop()

    with st.spinner("Vink is thinking..."):
        try:
            reply = get_gemini_reply(user_input)
            st.markdown(f'<div class="bot-bubble">🤖 <b>Vinks-reply:</b><br>{reply}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"⚠️ Vink Error: {e}")
            st.stop()

    with st.spinner("🔊 Speaking response..."):
        try:
            path = text_to_speech(reply)
            st.audio(path, format="audio/mp3", autoplay=True)
        except Exception as e:
            st.error("❌ Could not convert reply to audio.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:13px; color:gray;'>Powered by Google Gemini + Streamlit + gTTS</p>",
    unsafe_allow_html=True
)