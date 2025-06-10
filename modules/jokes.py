# modules/jokes.py

import random

JOKES = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you call fake spaghetti? An impasta!",
]

def tell_joke():
    return random.choice(JOKES)
