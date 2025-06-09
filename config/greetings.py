import random

RESPONSES = {
    "ella": [
        "Yes, my princess. How are you today?",
        "Hi Ella! I'm listening.",
        "What can I do for you, darling?",
        "Yes love, go ahead."
    ],
    "life": [
        "Yes champ! What's up?",
        "Yo Life! Talk to me.",
        "Daddy’s here, what’s on your mind?",
        "Sup superhero?"
    ],
    "default": [
        "Yes, how can I help?",
        "Hey there, go on.",
        "I’m listening.",
        "What’s up?"
    ]
}

def get_greeting(user):
    responses = RESPONSES.get(user, RESPONSES["default"])
    return random.choice(responses)
