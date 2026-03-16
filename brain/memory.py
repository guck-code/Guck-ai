import json

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_memory(memory, entry):
    memory.append(entry)

    # keep only last 100 memories
    if len(memory) > 100:
        memory = memory[-100:]

    save_memory(memory)
    return memory
