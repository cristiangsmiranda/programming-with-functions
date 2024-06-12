import re
def counting_words(filename, word):
    word_count = 0
    lines_with_word = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                words_in_line = re.findall(r'\b\w+\b', line.lower())
                for w in words_in_line:
                    if w == word.lower():
                        word_count += 1
                        lines_with_word.append(line_number)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None, None
    except UnicodeDecodeError as e:
        print(f"Unicode decode error: {e}")
        return None, None

    return word_count, lines_with_word

if __name__ == "__main__":
    filename = "Joseph_history.txt"
    word = input("Enter the word you want to count: ")

    count, lines = counting_words(filename, word)
    if count is not None:
        print(f"The word '{word}' occurs {count} times.")
        if lines:
            print(f"It appears on the following lines: {', '.join(map(str, lines))}")
        else:
            print("It does not appear in the text.")
