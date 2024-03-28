# Задача 6. Крестики-нолики
# Что нужно сделать
# Создайте программу, которая реализует игру «Крестики-нолики».
# Для этого напишите:
# 1. Класс, который будет описывать поле игры.
# class Board:
#     #  Класс поля, который создаёт у себя экземпляры клетки.
#     #  Пусть класс хранит информацию о состоянии поля (это может быть список
#     из девяти элементов).
#     #  Помимо этого, класс должен содержать методы:
#     #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка
#     не занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
#     True, иначе возвращается False.
#     #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает
#     True/False. True — если один из игроков победил, False — если победителя нет.
# 2. Класс, который будет описывать одну клетку поля:
# class Cell:
#     #  Клетка, у которой есть значения:
#     #  занята она или нет;
#     #  номер клетки;
#     #  символ, который клетка хранит (пустая, крестик, нолик).
# 3. Класс, который описывает поведение игрока:
# class Player:
#     #  У игрока может быть:
#     #  имя,
#     #  количество побед.
#     #  Класс должен содержать метод:
#     #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока
#     (номер клетки). Введённый номер нужно обязательно проверить.
# 4. Класс, который управляет ходом игры:
# class Game:
#     # класс «Игры» содержит атрибуты:
#     # состояние игры,
#     # игроки,
#     # поле.
#     # А также методы:
#     # Метод запуска одного хода игры. Получает одного из игроков, запрашивает
#     у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок
#     победил, возвращает True, иначе False.
#     # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
#     завершается победой одного из игроков или ничьей. Если игра завершена, метод
#     возвращает True, иначе False.
#     # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
#     игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий
#     счёт игроков.

import os
import random
import time


class Cell:
    def __init__(self, symbol=' '):
        self.symbol = symbol
        self.occupy = False
        if self.symbol != ' ':
            self.occupy = True


class Board:
    def __init__(self):
        self.dict_board = {'a1': Cell(), 'a2': Cell(), 'a3': Cell(),
                           'b1': Cell(), 'b2': Cell(), 'b3': Cell(),
                           'c1': Cell(), 'c2': Cell(), 'c3': Cell()}

    def draw_board(self):
        print(' ' * 5 + '1' + ' ' * 3 + '2' + ' ' * 3 + '3')
        print(' ' * 3 + '+' + '-' * 11 + '+')
        print('A' + ' ' * 2 + '| {a1} | {a2} | {a3} |'
              .format(a1=self.dict_board['a1'].symbol, a2=self.dict_board['a2'].symbol,
                      a3=self.dict_board['a3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')
        print('B' + ' ' * 2 + '| {b1} | {b2} | {b3} |'
              .format(b1=self.dict_board['b1'].symbol, b2=self.dict_board['b2'].symbol,
                      b3=self.dict_board['b3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')
        print('C' + ' ' * 2 + '| {c1} | {c2} | {c3} |'
              .format(c1=self.dict_board['c1'].symbol, c2=self.dict_board['c2'].symbol,
                      c3=self.dict_board['c3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')


class Player:
    def __init__(self):
        self.nickname = input('Enter your nickname: ')
        self.wins = 0
        self.symbol = input('Enter your marker-symbol: ')

    def make_turn(self, board):
        while True:
            turn = input(f'{self.nickname}, please, choose cell: ').lower()
            cell = board.dict_board.get(turn)
            if cell and not cell.occupy:
                cell.symbol = self.symbol
                cell.occupy = True
                return False
            else:
                print('Invalid cell or cell already occupied.\n'
                      'Please, choose other cell.')


class Computer:
    def __init__(self):
        self.nickname = 'Computer'
        self.wins = 0
        self.symbol = '@'  # '\u265E'

    def make_turn(self, board):
        while True:
            turn = random.choice(['a1', 'a2', 'a3',
                                  'b1', 'b2', 'b3',
                                  'c1', 'c2', 'c3'])
            time.sleep(2)
            cell = board.dict_board.get(turn)
            if cell and not cell.occupy:
                cell.symbol = self.symbol
                cell.occupy = True
                return False


class Game:
    def __init__(self):
        players = input('Choose type of game:\n'
                        '1. Player VS Computer\n'
                        '2. Player VS Player\n'
                        '>: ')
        if players == '1':
            self.player_1 = Player()
            self.player_2 = Computer()
            self.field = Board()
        elif players == '2':
            print('Player # 1:')
            self.player_1 = Player()
            print('Player # 2:')
            self.player_2 = Player()
            self.field = Board()
        else:
            print('Wrong type. Please enter "1" or "2".')

    def start_game(self):
        # os.system('cls')
        self.field.draw_board()
        self.player_1.make_turn(self.field)
        os.system('cls')
        self.field.draw_board()
        check_win(self.field, self.player_1)
        if isinstance(self.player_2, Computer):
            print('\nComputer is generating his turn...')
        self.player_2.make_turn(self.field)
        check_win(self.field, self.player_2)

    def score_table(self):
        print('+' + '-' * (len(self.player_1.nickname) + len(self.player_2.nickname) + 13) + '+')
        print(f'| {self.player_1.nickname} [{self.player_1.wins}] - [{self.player_2.wins}] {self.player_2.nickname} |')
        print('+' + '-' * (len(self.player_1.nickname) + len(self.player_2.nickname) + 13) + '+')


def header():
    name_of_programm = 'Tic-tac-toe game'
    print('+', '-' * (len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-' * (len(name_of_programm) - 8),
          'by ШелЛ +\n')


def start_new_game():
    new_game = Game()
    while True:
        os.system('cls')
        new_game.score_table()
        new_game.start_game()


def check_win(board, player):
    winning_combinations = [['a1', 'a2', 'a3'],
                            ['b1', 'b2', 'b3'],
                            ['c1', 'c2', 'c3'],
                            ['a1', 'b1', 'c1'],
                            ['a2', 'b2', 'c2'],
                            ['a3', 'b3', 'c3'],
                            ['a1', 'b2', 'c3'],
                            ['a3', 'b2', 'c1']]
    nobody_wins = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
    for combination in winning_combinations:
        if all(board.dict_board[cell].symbol == player.symbol for cell in combination):
            player.wins += 1
            print(f'{player.nickname} wins this part!')
            start_new_game()
            return True
    if all(board.dict_board[cell].symbol != ' ' for cell in board.dict_board):
        print(f'Drawn game!!')
        start_new_game()
        return True
    return False


header()
start_new_game()
