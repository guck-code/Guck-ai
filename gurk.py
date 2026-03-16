from brain.memory import load_memory, add_memory
from brain.thinker import think
import os

memory = load_memory()

print("Gurk AI online 🧠💥")

while True:
    user = input("human: ")

    # Run terminal commands if input is shell command
    if user.startswith(("cd ", "ls", "pwd")):
        os.system(user)
        continue

    reply = think(user, memory)
    print("Gurk:", reply)

    memory = add_memory(memory, {"human": user, "Gurk": reply})
