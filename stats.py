def get_num_words(book_text):
    return len(book_text.split())

def counting_caracters(book_text):
    counter = {}
    for character in book_text:
        char_lower = character.lower()
        if char_lower in counter:
            counter[char_lower] += 1
        else: counter[char_lower] = 1
    return counter     

def sort_on_num(item):
    return item["num"]

def sorted_dictionaries(char_count):
    char_sort = []
    for char in char_count:
        char_sort.append({"char": char, "num": char_count[char]})
    char_sort.sort(reverse=True, key=sort_on_num)
    #lambda is a quick way to write a function inline. instead of the helper funcion
    #char_sort.sort(reverse=True, key=lambda item: item["num"])
    return char_sort 