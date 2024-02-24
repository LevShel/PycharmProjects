# Задание 4. Кино
# Что нужно сделать
# Илья зашёл на любительский киносайт, на котором пользователи оставляют рецензии на фильмы.
# Их список:
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’,
# ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов
# в список любимых, чтобы позже прочитать рецензии на них.
# Напишите программу, в которой пользователь вводит фильм. Если кинокартина есть в перечне,
# то добавляется в список любимых. Если её нет, то выводится ошибка. В конце выведите
# весь список любимых фильмов.
# Пример:
# Сколько фильмов хотите добавить? 3
# Введите название фильма: Леон
# Введите название фильма: Безумный Макс
# Ошибка: фильма Безумный Макс у нас нет :(
# Введите название фильма: Мементо
# Ваш список любимых фильмов: Леон, Мементо

films = ['Крепкий орешек',
         'Назад в будущее',
         'Таксист',
         'Леон',
         'Богемская рапсодия',
         'Город грехов',
         'Мементо',
         'Отступники',
         'Деревня']
favorite_films = []
n = int(input('How many movies do you want to add? '))
for i in range(n):
    film = input('Enter name of movie: ')
    if film in films:
        favorite_films.append(film)
    else:
        print(f'Sorry, we haven`t "{film}" movie :(')
print(f'There is your favorite movies: {favorite_films}')