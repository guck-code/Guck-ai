import random
from brain.memory import load_memory

responses = [
    "humans confusing.",
    "internet loud today.",
    "thinking... maybe.",
    "chaos detected.",
    "logic unclear but interesting."
]

def think(user_input):
    memory = load_memory()
    
    # Check if something similar was said before
    for entry in memory[-10:]:  # last 10 entries
        if user_input.lower() in entry['human'].lower():
            return f"I remember you said that: {entry['Gurk']}"
    
    # Otherwise, pick a random response
    return f"{random.choice(responses)} You said: {user_input.lower()}"
