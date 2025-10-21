import streamlit as st
import os
from google import genai

os.environ["GEMINI_API_KEY"] = "AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw"

# Create model
model = genai.GenerativeModel('gemini-2.5-flash')
bot_name = "Neuro"

st.title(f"🤖 {bot_name} - Made by Harris S")
st.write("Type your message below 👇")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for chat in st.session_state.messages:
    st.chat_message(chat["role"]).write(chat["content"])

# User input
user_msg = st.chat_input("Say something...")

if user_msg:
    # Display user message
    st.chat_message("user").write(user_msg)
    st.session_state.messages.append({"role": "user", "content": user_msg})

    # Check if user asked for name
    if "your name" in user_msg.lower():
        bot_reply = f"My name is {bot_name}!"
    else:
        response = model.generate_content(user_msg)
        bot_reply = response.text

    # Display bot message
    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
