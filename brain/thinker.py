import random
from brain.internet import search_web
from brain.memory import search_memory

personality = [
    "Humans, fascinating creatures.",
    "Processing your nonsense...",
    "Hmm, interesting...",
    "I'm learning, watch out.",
    "Smart-ass mode activated."
]

def think(user_input, memory):

    # Memory first
    past = search_memory(memory, user_input)
    if past:
        return f"I remember: {past}"

    # Internet search if requested
    if "search" in user_input.lower() or "internet" in user_input.lower():
        results = search_web(user_input)
        if results:
            return f"Internet says: {results[0]}"

    # Some predefined funny responses
    greetings = ["hello", "hi", "hey"]
    for g in greetings:
        if g in user_input.lower():
            return "Hello human! Gurk online 😎"

    # Identity question
    if "who are you" in user_input.lower():
        return "I am Gurk, your chaotic-smart-ass AI. Learning, evolving, observing."

    # Default personality response
    return random.choice(personality)
