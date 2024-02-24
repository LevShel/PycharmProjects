# Задание 5. Контейнеры
# Что нужно сделать
# Контейнеры на складе лежат в ряд в порядке невозрастания (меньше либо равно) массы
# в килограммах. На склад привезли ещё один контейнер, который тоже нужно положить
# на определённое место.
# Напишите программу, которая получает на вход невозрастающую последовательность
# натуральных чисел. Они означают массу каждого контейнера в ряду. После этого вводится
# число X — масса нового контейнера. Программа выводит номер, под которым будет лежать
# новый контейнер. Если в ряду есть контейнеры с массой, как у нового, то его нужно
# положить после них.
# Обеспечьте контроль ввода: все числа не превышают 200.
# Пример:
# Количество контейнеров: 8
# Введите вес контейнера: 165
# Введите вес контейнера: 163
# Введите вес контейнера: 160
# Введите вес контейнера: 160
# Введите вес контейнера: 157
# Введите вес контейнера: 157
# Введите вес контейнера: 155
# Введите вес контейнера: 154
# Введите вес нового контейнера: 162
# Номер, который получит новый контейнер: 3

def position(new_weight, weights):
    position_number = 1
    for weight in weights:
        if new_weight <= weight:
            position_number = weights.index(weight) + 2
    return position_number


containers = []
n = int(input('Number of containers: '))
for i in range(1, n + 1):
    container = int(input(f'Enter weight of {i} container: '))
    containers.append(container)
x = int(input('Enter weight of new container: '))
if x > 200 or any(container > 200 for container in containers):
    print('Error! All numbers must be no more than 200.')
number = position(x, containers)
print(f'The number that the new container will receive: {number}')
