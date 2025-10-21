import streamlit as st
import os
from google import genai

os.environ["GEMINI_API_KEY"] = "AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw"

model = 'gemini-2.5-flash'
bot_name = "Neuro"

st.title(f"🤖 {bot_name} - Made by Harris S")
st.write("Type your message below 👇")

if "messages" not in st.session_state:
    st.session_state.messages = []

for chat in st.session_state.messages:
    st.chat_message(chat["role"]).write(chat["content"])

user_msg = st.chat_input("Say something...")

if user_msg:
    st.chat_message("user").write(user_msg)
    st.session_state.messages.append({"role": "user", "content": user_msg})

    # Generate a response using the genai library
    bot_reply = genai.generate_response(model=model, prompt=user_msg)

    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    