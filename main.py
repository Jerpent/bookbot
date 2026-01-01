from stats import count_words, count_letters
import sys

def sort_on(letter_count):
    return (letter_count[1])

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    sorted_letters = dict(sorted(letter_count.items(), reverse=True, key=sort_on))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_letters.items():
        print(f"{letter}: {count}")
    print("============= END ===============")

main()