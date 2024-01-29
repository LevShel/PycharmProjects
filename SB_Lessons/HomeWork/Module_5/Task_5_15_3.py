# Задача 3. Поступление
# Что нужно сделать
# В университете на факультет кибернетики очень серьёзный конкурс — поступают только сильнейшие,
# первые десять человек из списка. Потом среди поступивших определяется, кто будет
# получать стипендию. Для стипендии общий балл при поступлении должен быть не менее 290.
# Напишите программу, которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.
# Пример 1:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 295
# Поздравляем, вы поступили!
# Бонусом вам будет начисляться стипендия.
# Пример 2:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 270
# Поздравляем, вы поступили!
# Но вам не хватило баллов для стипендии.
# Пример 3:
# Введите место в списке поступающих: 11
# К сожалению, вы не поступили.

place = int(input('Enter your place in list: '))

if place <= 10:
    score = int(input('Enter your total score: '))
    print('Congratulations, you got in!')
    if score > 290:
        print('A scholarship will be awarded to you as a bonus.')
    else:
        print('But you didn`t have enough points for the scholarship.')
else:
    print('Unfortunately, you didn`t get in.')