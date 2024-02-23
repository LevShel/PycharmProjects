# Задача 7. Недоделка
# Что нужно сделать
# Вы пришли на работу в компанию по разработке игр, целевая аудитория —
# дети и их родители. У предыдущего программиста было задание сделать две игры
# в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист,
# на место которого вы пришли, перед увольнением не успел выполнить эту задачу
# и оставил только небольшой шаблон проекта. Используя этот шаблон, реализуйте игры «Камень,
# ножницы, бумага» и «Угадай число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку
# и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу,
# бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор,
# пока он не отгадает загаданное.
# def rock_paper_scissors():
#   # Здесь будет игра «Камень, ножницы, бумага»
# def guess_the_number():
#   # Здесь будет игра «Угадай число»
# def mainMenu():
#   # Здесь главное меню игры
# mainMenu():
#   pass

import random
import time
import os


def rock_paper_scissors():  # игра "камень/ножницы/бумага"
    name_of_programm = 'Игра "Камень, ножницы, бумага..."'
    print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
          'by ШелЛ +\n')
    while True:
        # comp_score = 0
        # user_score = 0
        # print(f'comp [{comp_score}] - [{user_score}] user')
        time.sleep(1)
        print('\nКамень', end=', ')
        time.sleep(1)
        print('ножницы', end=', ')
        time.sleep(1)
        print('бумага', end='...')
        time.sleep(1)
        print('\nРаз', end=', ')
        time.sleep(1)
        print('два', end=', ')
        time.sleep(1)
        print('три!')
        user_step = input('>: ').lower()
        rps = ['камень', 'ножницы', 'бумага']
        if user_step != 'стоп':
            comp_step = random.choice(rps)
            print('         ', comp_step)
            if comp_step == user_step:
                print('Ничья!')
            elif comp_step == 'камень' and user_step == 'ножницы':
                print('Комп выиграл!')
            elif comp_step == 'камень' and user_step == 'бумага':
                print('Ты выиграл!')
            elif comp_step == 'ножницы' and user_step == 'камень':
                print('Ты выиграл!')
            elif comp_step == 'ножницы' and user_step == 'бумага':
                print('Комп выиграл!')
            elif comp_step == 'бумага' and user_step == 'камень':
                print('Комп выиграл!')
            elif comp_step == 'бумага' and user_step == 'ножницы':
                print('Ты выиграл!')
            elif user_step == 'стоп':
                print('Игра завершена!')
                # exit()
                break
            else:
                print('Ошибка! Напиши камень/ножницы/бумага.')
        else:
            print('Игра завершена!')
            break
        # os.system('cls')


def guess_the_number():  # игра "угадай число"
    name_of_programm = 'Игра "Угадай число!"'
    print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
          'by ШелЛ +\n')
    while True:
        start_num = random.randint(1, 10)
        end_num = random.randint(11, 20)
        hidden_num = random.randint(start_num, end_num)
        print(f'Загадано число в диапазоне от {start_num} до {end_num}...')
        guess = int(input('Угадывай: '))
        while hidden_num != guess:
            print('Не угадал!')
            guess = int(input('Попробуй ещё раз: '))
            if guess == 0:
                print('Игра завершена!')
                break
        print('     Угадал!')
        # exit()
        print('Игра завершена!')
        break


def main_menu():    # главное меню
    while True:
        print('\nВыбери игру:\n'
              '1. "Камень, ножницы, бумага...".\n'
              '2. "Угадай число!".')
        user_choice = input(':> ')
        if user_choice == '1':
            rock_paper_scissors()
        elif user_choice == '2':
            guess_the_number()
        else:
            print('Ошибка! Выбери номер игры из меню.')
            # user_choice = input(':> ')


# Шапка программы
name_of_programm = 'Мини-игры'
print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
      'by ШелЛ +\n')

# Тело программы
main_menu()
