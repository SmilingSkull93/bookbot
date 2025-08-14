import sys
from stats import (
    get_num_words, 
    counting_caracters,
    sorted_dictionaries
)


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = counting_caracters(book_text)
    sorted_counts = sorted_dictionaries(char_count)
    print_report(book_path, num_words, sorted_counts)   


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def print_report(book_path, num_words, sorted_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        char = item["char"]
        num = item["num"]
        # If you want only alphabetic chars, use .isalpha()!
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ==============")


main()