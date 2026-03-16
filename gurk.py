from brain.memory import load_memory, add_memory
from brain.thinker import think

memory = load_memory()

print("Gurk AI online")

while True:

    user = input("human: ")

    reply = think(user)

    print("Gurk:", reply)

    memory = add_memory(memory, {
        "human": user,
        "Gurk": reply
    })
