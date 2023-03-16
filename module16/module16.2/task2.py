staff_count = int(input('Кол-во сотрудников: '))
salary_list = []

for i in range(staff_count):
    salary = int(input(f'Зарплата {i + 1} сотрудника: '))
    salary_list.append(salary)

for i_salary in salary_list:
    if i_salary == 0:
        salary_list.remove(i_salary)
print('\nОсталось сотрудников:', len(salary_list))
print('Зарплаты:', salary_list)
print('Максимальная зп:', max(salary_list))
print('Минимальная  зп:', min(salary_list))
