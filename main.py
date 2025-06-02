import sys

from stats import word_count

from stats import character_count

from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = word_count(text)
    characters = character_count(text)
    sorted = sort_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for d in sorted:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
 
main()
