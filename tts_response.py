import os
from dotenv import load_dotenv

load_dotenv()

DEV_MODE = os.getenv("DEV_MODE", "true").lower() == "true"

if not DEV_MODE:
    import pyttsx3

def speak(text):
    if DEV_MODE:
        print(f"(Voice simulated): {text}")
    else:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
