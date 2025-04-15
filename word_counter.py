def preprocess_text(text):
    forbidden_chars = [".", ",", ";", "\n"]
    index = 0
    while index < len(forbidden_chars):
        text = text.replace(forbidden_chars[index], " ")
        index += 1
    return text


def count_word_occurrences(word, text):
    word = word.lower()
    text = preprocess_text(text.lower())
    words = text.split(" ")

    count = 0
    index = 0

    while index < len(words):
        if words[index] != "":
            if words[index] == word:
                count += 1
        index += 1
    return f"{count} ocurrencias encontradas."
