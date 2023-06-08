file = None
try:
    file = open('23.3.txt', 'w', encoding='utf-8')
    number = int(input('Введите строку: '))
    file.write(str(number))
except (FileNotFoundError, PermissionError):
    print('Проблема при открытии файла.')
except ValueError:
    print('Нельзя преобразовать данные в целое.')
except Exception:
    print('Неожиданная ошибка.')
else:
    print('Запись прошла без ошибок')
finally:
    if file and not file.closed:
        file.close()
