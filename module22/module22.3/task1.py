import os

path_to_first = os.path.abspath(os.path.join('task', 'group_1.txt'))
path_to_second = os.path.abspath(os.path.join('task', 'Additional_info', 'group_2.txt'))

file_1 = open(path_to_first, 'r', encoding='utf-8')
file_2 = open(path_to_second, 'r', encoding='utf-8')

summa = 0
diff = 0
compose = 1

for i_line in file_1:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])

for i_line in file_2:
    info = i_line.split()
    if info:
        compose *= int(info[2])

file_1.close()
file_2.close()

print('Сумма очков первой группы:', summa)
print('Разность очков первой группы:', diff)
print('Произведение очков второй группы:', compose)
