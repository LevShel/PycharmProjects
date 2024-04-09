# Задача 2. Карма
# Что нужно сделать
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать
# 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает количество
# кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
# •	KillError,
# •	DrunkError,
# •	CarCrashError,
# •	GluttonyError,
# •	DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого
# возможен только при накоплении кармы до уровня константы. Исключения обработайте
# и запишите в отдельный лог karma.log.
# По итогу у вас может быть примерно такая структура программы:
# открываем файл
# цикл по набору кармы
#    try
#       карма += one_day()
#    except(ы) с указанием классов исключений, которые нужно поймать
#       добавляем запись в файл
# закрываем файл

import random
import time


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    karma = random.randint(1, 7)
    return karma


with open('karma.log', 'w') as file:
    total_karma = 0
    day = 0
    while total_karma < 500:
        time.sleep(1)
        day += 1
        print(f'Day {day}: ', end='')
        file.write(f'Day {day}: ')
        try:
            random_error = random.randint(1, 10)
            if random_error == 1:
                exception_message = random.randint(1, 5)
                if exception_message == 1:
                    raise KillError()
                elif exception_message == 2:
                    raise DrunkError()
                elif exception_message == 3:
                    raise CarCrashError()
                elif exception_message == 4:
                    raise GluttonyError()
                elif exception_message == 5:
                    raise DepressionError()
            else:
                total_karma += one_day()
                print(total_karma)
                file.write(str(f'{total_karma}\n'))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            print(f'Исключение: {type(e).__name__}')
            file.write(f'Исключение: {type(e).__name__}\n')
