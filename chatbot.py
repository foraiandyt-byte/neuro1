import google.generativeai as genai

genai.configure(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")


def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")  # fast + free
    response = model.generate_content(prompt)
    return response.text

def run_chatbot():
    print("🤖 ChatGPT-style Chatbot (Gemini Free) — type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        reply = chat_with_gemini(user_input)
        print("Bot:", reply)

run_chatbot()
