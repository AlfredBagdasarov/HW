def is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False

films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня', 'Побег из Шоушенка',

    'Проклятый остров', 'Начало', 'Матрица', 'Бойцовский клуб']

top_list = []
while True:
    print('Ваш текущий топ фильмов:', top_list)
    new_movie = input('\nНазвание фильма: ')
    if is_film_exist(new_movie, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            if is_film_exist(new_movie, top_list):
                print('Фильм с таким названием уже есть в вашем списке.')
            else:
                top_list.append(new_movie)
        if command == 'вставить':
            index = int(input('На какое место? '))
            top_list.insert(index - 1, new_movie)
        if command == 'удалить':
            if is_film_exist(new_movie, top_list):
                top_list.remove(new_movie)
            else:
                print('Такого фильма нет в вашем списке.')
    else:
        print('Такого фильма нет на сайте.')