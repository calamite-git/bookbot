import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Analyze a text file and report word and character frequencies.")
    parser.add_argument("book_path", help="Path to the book text file")
    args = parser.parse_args()

    # Read the book text from the provided path
    text = read_book_text(args.book_path)
    word_count = count_words(text)
    char_frequency = calculate_char_frequency(text)
    sorted_char_list = sort_char_frequency(char_frequency)

    # Print the results
    print(f"--- BookBot Analysis Report ---")
    print(f"Total Words: {word_count}")
    print()

    print("Letter Frequency:")
    for char_info in sorted_char_list:
        char = char_info["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {char_info['num']} ")

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
