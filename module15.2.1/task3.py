staff_count = int(input('Кол-во сотрудников в офисе: '))
staff_list =[]

for _ in range(staff_count):
    employee_ID = int(input('ID сотрудника: '))
    if employee_ID > 0:
        staff_list.append(employee_ID)
    else:
        print('Ошибка ввода! ID сотрудника не может быть отрицательным!')

search_ID = int(input('Какой ID ищем? '))

if search_ID not in staff_list:
    print('Сотрудник не работает!')
else:
    print('Сотрудник на месте')