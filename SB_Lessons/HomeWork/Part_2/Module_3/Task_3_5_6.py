# Задание 6. Ролики
# Что нужно сделать
# Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть
# ролики только своего размера.
# Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек может одновременно
# взять ролики и пойти кататься.
# Пример:
# Количество роликов: 4
# Размер пары 1: 41
# Размер пары 2: 40
# Размер пары 3: 39
# Размер пары 4: 42
#
# Количество людей: 3
# Размер ноги человека 1: 42
# Размер ноги человека 2: 41
# Размер ноги человека 3: 42
# Наибольшее количество людей, которые могут взять ролики: 2

skates = []
peoples = []
possible = 0

num_skates = int(input('Num of skates: '))
for size in range(1, num_skates+1):
    skate_size = int(input(f'Size of {size} pair: '))
    skates.append(skate_size)

num_peoples = int(input('Num of peoples: '))
for size in range(1, num_peoples+1):
    foot_size = int(input(f'Size of {size} pair: '))
    peoples.append(foot_size)

for foot_size in peoples:
    if foot_size in skates:
        possible += 1
        skates.remove(foot_size)

print(f'The largest number of people who can take skates: {possible}')