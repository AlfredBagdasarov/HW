words = [input('Введите слово: ') for _ in range(3)]
text = input('Введите текст: ')
words_count = [text.count(word) for word in words]

print('Кол-во слов в тексте:', words_count)
