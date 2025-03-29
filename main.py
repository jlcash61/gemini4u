# main.py
from assistant import GeminiAssistant

def main():
    assistant = GeminiAssistant()
    print("🤖 Gemini Assistant (REST API) is ready. Type your message, or 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        response = assistant.ask(user_input)
        print(f"Gemini: {response}\n")

if __name__ == "__main__":
    main()
