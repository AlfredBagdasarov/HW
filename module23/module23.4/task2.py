def check_palindrome(word):
    return word == word[::-1]


with open('words.txt', 'r', encoding='utf-8'
          ) as file, open('errors.log',
                          'w', encoding='utf-8') as log_file:
    count = 0

    for i_line in file:
        try:
            clear_line = i_line.rstrip()
            if clear_line.isalpha():
                count += check_palindrome(clear_line)
            else:
                raise ValueError('строка "{}" не полностью состоит из букв\n'.format(i_line))
        except ValueError as exc:
            log_file.write(str(exc))
    print(count)
