def main():
    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)
    word_count = count_words(text)
    char_frequency = calculate_char_frequency(text)
    sorted_char_list = sort_char_frequency(char_frequency)

    print(f"--- BookBot Analysis Report ---")
    print(f"{word_count} words found in the document")
    print()

    for char_info in sorted_char_list:
        char = char_info["char"]
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {char_info['num']} times")
        

def read_book_text(path):
    """Reads and returns the text from the given file path."""
    with open(path, "r") as file:
        return file.read()


def count_words(text):
    """Counts and returns the number of words in the text."""
    return len(text.split())


def calculate_char_frequency(text):
    """Calculates and returns a dictionary of character frequencies."""
    char_freq = {}
    for char in text:
        lower_char = char.lower()
        char_freq[lower_char] = char_freq.get(lower_char, 0) + 1
    return char_freq


def sort_char_frequency(char_freq):
    """Converts the character frequency dictionary to a sorted list."""
    sorted_list = [
        {"char": char, "num": count} for char, count in char_freq.items()
    ]
    return sorted(sorted_list, key=lambda x: x["num"], reverse=True)


if __name__ == "__main__":
    main()
