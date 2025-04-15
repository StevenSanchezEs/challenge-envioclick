def preprocess_text(text):
    forbidden_chars = [".", ",", ";", "\n"]
    index = 0
    while index < len(forbidden_chars):
        text = text.replace(forbidden_chars[index], " ")
        index += 1
    return text
