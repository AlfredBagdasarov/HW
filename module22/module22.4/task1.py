read_file = open('numbers.txt', 'r', encoding='utf-8')
summ = 0
for i_line in read_file:
    clear_line = i_line.rstrip()
    if clear_line:
        summ += int(clear_line)
read_file.close()

write_file = open('answer.txt', 'w', encoding='utf-8')
write_file.write(str(summ))
write_file.close()
