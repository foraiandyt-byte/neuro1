import streamlit as st
from google import genai

# Configure your Gemini API key
genai.api_key = "AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw"

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Gemini Chatbot 💬")

# Input box
user_input = st.text_input("Type your message:")

# Send button
if st.button("Send") and user_input:
    # Add user message
    st.session_state.chat_history.append(f"You: {user_input}")
    
    # Call Gemini API
    try:
        response = genai.Text.generate(
            model="gemini-2.5",
            prompt=user_input,
            max_output_tokens=200
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {e}"

    # Add bot response
    st.session_state.chat_history.append(f"Bot: {bot_reply}")

# Display chat history
for msg in st.session_state.chat_history:
    st.write(msg)

    