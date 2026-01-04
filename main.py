from stats import get_num_words, get_char_count, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def get_filepath():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]
    
def main():
    frankenstein_text = get_book_text(get_filepath())
    num_words = get_num_words(frankenstein_text)
    char_count = sort_char_count(get_char_count(frankenstein_text))
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for char_dict in char_count:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print('============= END ===============')
    
main()