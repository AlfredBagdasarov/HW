string = set(input('Введите строку: '))
nums_set = set()
for sym in string:
    if '0' <= sym <= '9':
        nums_set.add(sym)
print(''.join(sorted(nums_set)))
# 2-й способ
string = set(input('Введите строку: '))
nums_set = sorted(string & set('0123456789'))
print(''.join(nums_set))
