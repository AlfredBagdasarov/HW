# alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

code_message = [alphabet[(alphabet.index(letter) + shift) % len(alphabet)] if letter in alphabet
                else letter for letter in message.lower()]
print('Зашифрованное сообщение:', ''.join(code_message))
