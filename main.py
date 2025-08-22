import sys

from stats import get_char_occurencies, get_number_of_words, order_chars_dict


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text


def print_report(word_counts, char_count, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    for char in char_count:
        if char["char"].isalpha():
            tmp_char = char["char"]
            tmp_num = char["num"]
            print(f"{tmp_char}: {tmp_num}")
    print("============= END ===============")


def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_number_of_words(book_text)
    char_occurencies = get_char_occurencies(book_text)
    char_dict = order_chars_dict(char_occurencies)
    print_report(num_words, char_dict, filepath)
    return


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
