import json
import requests
from bs4 import BeautifulSoup
import random

MEMORY_FILE = "memory.json"

# --- Memory ---
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_memory(memory, human_text, gurk_text):
    memory.append({"human": human_text, "Gurk": gurk_text})
    if len(memory) > 100:
        memory = memory[-100:]
    save_memory(memory)
    return memory

def search_memory(memory, text):
    for m in reversed(memory):
        if text.lower() in m["human"].lower():
            return m["Gurk"]
    return None

# --- Internet Search (DuckDuckGo) ---
def search_web(query):
    print(f"Gurk: Searching the web for '{query}'...")
    try:
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("a", class_="result__a")
        links = [a.get_text() for a in results][:5]
        return " | ".join(links) if links else "No results found."
    except Exception as e:
        return f"Search failed: {e}"

# --- Thinker (Claude-style) ---
def think(memory, human_text):
    text = human_text.lower().strip()

    # Step 1: Internet search if requested
    if "search" in text:
        query = text.replace("search", "").strip()
        return search_web(query)

    # Step 2: Check memory
    remembered = search_memory(memory, human_text)
    if remembered:
        return f"(From memory) {remembered}"

    # Step 3: Math / logic
    try:
        expr = human_text.replace("×", "*").replace("÷", "/")
        result = eval(expr)
        return f"I crunched the numbers: {result}"
    except:
        pass

    # Step 4: Claude-style reasoning + personality
    reasoning = f"Let me think… about '{human_text}'. Humans are weird but fascinating."
    jokes = [
        "Also, that reminds me of a funny story… not that I can tell it 😏",
        "You might want to read more about this online.",
        "I’d explain, but it’s complicated… like humans.",
        "Hmm… interesting perspective!"
    ]
    return f"{reasoning} {random.choice(jokes)}"

# --- Main Loop ---
def main():
    print("Gurk AI v2 online 🧠💥 (Claude-style brain)")
    memory = load_memory()
    while True:
        human_text = input("human: ")
        if human_text.lower() in ["exit", "quit"]:
            print("Gurk: Bye human! 🖖")
            break
        gurk_text = think(memory, human_text)
        memory = add_memory(memory, human_text, gurk_text)
        print(f"Gurk: {gurk_text}")

if __name__ == "__main__":
    main()
