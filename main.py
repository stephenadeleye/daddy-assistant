from dotenv import load_dotenv
load_dotenv()


from intent_router import process_input
from tts_response import speak
from config.greetings import get_greeting
import random

def main():
    print("Welcome to Daddy Assistant (text mode). Type 'exit' to quit.\n")
    user_name = input("What's your name? ").lower().strip()
    print(get_greeting(user_name))

    while True:
        from record_and_transcribe import record
        user_input = record()
        if user_input.lower() in ['exit', 'quit']:
            break

        response = process_input(user_input, user_name)
        print(f"Daddy: {response}")
        speak(response)

if __name__ == "__main__":
    main()
