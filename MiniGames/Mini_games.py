import random
import time
import os


def rock_paper_scissors():  # игра "камень/ножницы/бумага"
    # Шапка
    name_of_programm = 'Игра "Камень, ножницы, бумага..."'
    print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
          'by ШелЛ +\n')
    print('Для выхода из игры введите "стоп".')
    # Игра
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
    # Шапка
    name_of_programm = 'Игра "Угадай число!"'
    print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
          'by ШелЛ +\n')
    print('Для выхода из игры введите "0".')
    # Игра
    while True:
        start_num = random.randint(1, 10)
        end_num = random.randint(11, 20)
        hidden_num = random.randint(start_num, end_num)
        print(f'\nЗагадано число в диапазоне от {start_num} до {end_num}...')
        guess = int(input('Угадывай: '))
        if guess == 0:
            print('Игра завершена!')
            break
        else:
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


def main_menu():  # главное меню
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
name_of_programm = 'М И Н И - И Г Р Ы'
print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
      'by ШелЛ +\n')

# Тело программы
main_menu()
