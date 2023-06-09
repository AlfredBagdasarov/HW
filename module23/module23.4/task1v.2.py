people_file = open('people.txt', 'r', encoding='utf8')
result = 0
for line in people_file:
    clear_line_len = len(line.rstrip())
    result += clear_line_len
    if clear_line_len < 3:
        raise Exception

print(result)
