def get_number_of_words(book_text: str):
    return len(book_text.split())


def get_char_occurencies(book_text: str):
    book_text = book_text.lower()

    words = book_text.split()

    char_dict = {}
    for word in words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict


def order_chars_dict(char_dict: dict):
    list = []
    for key, value in char_dict.items():
        list.append({"char": key, "num": value})

    list.sort(reverse=True, key=lambda items: items["num"])
    return list
