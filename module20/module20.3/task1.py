string = input('Введите строку: ')

for index, sym in enumerate(string):
    if sym == '~':
        print(index)


# Второй способ решения:
def get_indexes(where_to_search, what_to_search):
    return [str(i) for i, letter in enumerate(where_to_search) if letter == what_to_search]


text = input("Введите текст: ")
print("Ответ:", " ".join(get_indexes(text, "~")))
