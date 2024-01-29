# Задача 8. Игра «Компьютер угадывает число»
# Что нужно сделать
# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из трёх чисел:
# 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
# При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.


#### Вариант для долгой игры с большим количеством попыток: ####
import random
attempt = 0
print('I`ll try to guess your num from 1 to 10...')
comp_answer = random.randint(1, 10)
while True:
    attempt += 1
    print(f'It is {comp_answer} ?', end=' ')
    my_answer = input('Y/N : ').upper()
    if my_answer == 'N':
        comp_question = input('The number is less (-) or more (+) than necessary? ')
        if comp_question == '+':
            comp_answer = random.randint(comp_answer, 10)
        else:
            comp_answer = random.randint(1, comp_answer)
    else:
        print(f'I guessed it! Number of attempts: {attempt}.')
        break

#### Вариант для 7 попыток, используя алгоритм бинарного поиска: ####

# def guess_number():
#     print("Загадайте число от 1 до 100 включительно.")
#
#     lower_bound = 1
#     upper_bound = 100
#     attempts = 0
#
#     while True:
#         middle = (lower_bound + upper_bound) // 2
#         attempts += 1
#
#         response = int(input(f"Твоё число равно, меньше или больше, чем {middle}? "
#                              f"(1 - равно, 2 - больше, 3 - меньше): "))
#
#         if response == 1:
#             print(f"Компьютер угадал число {middle} за {attempts} попыток.")
#             break
#         elif response == 2:
#             lower_bound = middle + 1
#         elif response == 3:
#             upper_bound = middle - 1
#         else:
#             print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")
#
#         if attempts >= 7:
#             print("Компьютер не смог угадать число за 7 попыток. "
#                   "Загаданное число может быть слишком сложным.")
#
# guess_number()