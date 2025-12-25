import sys
from stats import get_num_words, get_character_count, get_sorted_characters


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_counts = get_character_count(text)
    sorted_chars = get_sorted_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()