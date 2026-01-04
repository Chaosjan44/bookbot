def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict.keys():
            char_dict[char] = 1
            continue
        char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items['num']

def sort_char_count(char_dict):
    char_array = []
    for char in char_dict:
        char_array.append({'char': char, 'num': char_dict[char]})
    char_array.sort(reverse=True, key=sort_on)
    return char_array