import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match(r'wo', text)
print('Поиск шаблона в начале строки:', result)

result = re.search(r'wo', text)
print('Поиск первого найденного совпадения по шаблону:', result)
print('Содержимое найденной подстроки:', result.group(0))
print('Начальная позиция:', result.start())
print('Конечная позиция:', result.end())
result = re.findall(r'wo', text)
print('Список всех упоминаний шаблона:', result)
result = re.sub(r'wo', 'ЗАМЕНА', text)
print('Текст после замены:', result)
