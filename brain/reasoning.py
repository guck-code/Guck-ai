def analyze(user_input):

    text = user_input.lower()

    if "who" in text:
        return "identity"

    if "what" in text:
        return "definition"

    if "why" in text:
        return "reasoning"

    if "how" in text:
        return "instruction"

    if "hello" in text or "hi" in text:
        return "greeting"

    return "general"
