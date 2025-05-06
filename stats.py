def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    chars_count = {}
    for char in text:
        char_low = char.lower()
        if char_low not in chars_count:
            chars_count[char_low] = 0
        chars_count[char_low] += 1

    return chars_count

def sort_on(dict):
    return dict["num"]

def create_sorted_list(unsorted_dictionary):
    sorted_list = []
    for char, count in unsorted_dictionary.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
