import streamlit as st
import os
from google import genai

os.environ["GEMINI_API_KEY"] = "AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw"

model = genai.Model('gemini-2.5-flash')
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


    if "your name" in user_msg.lower():
        bot_reply = f"My name is {bot_name}!"
    else:
        response = model.generate_content(user_msg)
        bot_reply = response.text


    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    