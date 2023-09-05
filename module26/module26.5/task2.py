def number_from_text(text):
    return [int(number) for number in text.rstrip().split()]


def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(number_from_text(line))
            yield clear_line_sum


all_sum = 0
for i_number in file_parser('numbers.txt'):
    all_sum += i_number
print(all_sum)
