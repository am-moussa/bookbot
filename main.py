import sys
from stats import word_count, char_count, char_count_sorted


args = sys.argv

if len(args) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

def main(file_path):
    print(f"Found {word_count(get_book_text(file_path))} total words")
    for i in char_count_sorted(char_count(get_book_text(file_path))):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
            


if __name__ == "__main__":
    main(args[1])