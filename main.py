from sys import argv
from stats import get_num_words, get_letter_counts, get_sorted_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
    path_to_book = argv[1]
    letterCount = get_letter_counts(path_to_book)
    print("=========== BOOKBOT =============")
    print(f"Analyzing book found at {path_to_book}...")
    print("---------- Word Count -----------")
    print(f"Found {get_num_words(path_to_book)} total words")
    print("-------- Character Count --------")
    get_sorted_report(letterCount)

main()