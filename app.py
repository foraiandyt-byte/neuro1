import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Gemini Chatbot 💬")

# Input box
user_input = st.text_input("Type your message:")

# Send button
if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(f"You: {user_input}")
    
    # Create Gen AI client
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  # ⬅️ Replace with your real Gemini API key
    
    # Call Gemini API
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {e}"

    # Add bot response to chat history
    st.session_state.chat_history.append(f"Bot: {bot_reply}")

# Display chat history
for msg in st.session_state.chat_history:
    st.write(msg)
