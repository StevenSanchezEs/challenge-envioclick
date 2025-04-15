import sys


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


def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <texto> <palabra>")
        sys.exit(1)

    text = sys.argv[1]
    word = sys.argv[2]
    result = count_word_occurrences(word, text)
    print(result)


if __name__ == "__main__":
    main()
