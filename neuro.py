import google.genai as genai

client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  # ⬅️ Replace with your real Gemini API key


# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! 👋")
        break

    try:
        # Generate response using Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # You can change to "gemini-1.5-pro" for deeper answers
            contents=user_input
        )

        print("Chatbot:", response.output_text)

    except Exception as e:
        print(f"⚠️ Error: {e}")