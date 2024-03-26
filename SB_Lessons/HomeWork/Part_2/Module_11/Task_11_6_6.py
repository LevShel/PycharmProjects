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
              .format(a1=self.dict_board['a1'].symbol, a2=self.dict_board['a2'].symbol, a3=self.dict_board['a3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')
        print('B' + ' ' * 2 + '| {b1} | {b2} | {b3} |'
              .format(b1=self.dict_board['b1'].symbol, b2=self.dict_board['b2'].symbol, b3=self.dict_board['b3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')
        print('C' + ' ' * 2 + '| {c1} | {c2} | {c3} |'
              .format(c1=self.dict_board['c1'].symbol, c2=self.dict_board['c2'].symbol, c3=self.dict_board['c3'].symbol))
        print(' ' * 3 + '+' + '-' * 11 + '+')


class Player:
    def __init__(self):
        self.nickname = input('Enter your nickname: ')
        self.wins = 0
        self.symbol = input('Enter your marker-symbol: ')

    def make_turn(self, board):
        turn = input('Choose cell: ').lower()
        cell = board.dict_board.get(turn)
        if cell and not cell.occupy:
            cell.symbol = self.symbol
            cell.occupy = True
        else:
            print('Invalid cell or cell already occupied.')


field = Board()
field.draw_board()
player_1 = Player()
player_2 = Player()
while True:
    player_1.make_turn(field)
    field.draw_board()

    player_2.make_turn(field)
    field.draw_board()

#           CHAT GPT:
# class Cell:
#     def __init__(self, number):
#         self.number = number  # Номер клетки
#         self.symbol = " "  # Символ клетки (" ", "X", "O")
#
#     def occupy(self, symbol):
#         if self.symbol == " ":
#             self.symbol = symbol
#             return True
#         else:
#             return False
#
#
# class Board:
#     def __init__(self):
#         self.cells = [Cell(i) for i in range(1, 10)]  # Создание клеток
#
#     def display(self):
#         print()
#         print(' ' * 4 + 'A' + ' ' * 3 + 'B' + ' ' * 3 + 'C')
#         print(' ' * 2 + '+' + "-" * 11 + '+')
#         j = 1
#         for i in range(0, 9, 3):
#             print(f'{j} |', end='')
#             print(f' {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |')
#             j += 1
#             if i < 7:
#                 print(' ' * 2 + '+' + "-" * 11 + '+')
#         print()
#
#     def check_winner(self, symbol):
#         # Проверка строк
#         for i in range(0, 9, 3):
#             if self.cells[i].symbol == self.cells[i + 1].symbol == self.cells[i + 2].symbol == symbol:
#                 return True
#         # Проверка столбцов
#         for i in range(3):
#             if self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol == symbol:
#                 return True
#         # Проверка диагоналей
#         if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol == symbol:
#             return True
#         if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol == symbol:
#             return True
#         return False
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.wins = 0
#
#     def make_move(self, board):
#         while True:
#             move = input(f"{self.name}, enter cell number (1-9): ")
#             if move.isdigit() and 1 <= int(move) <= 9:
#                 cell_number = int(move)
#                 if board.cells[cell_number - 1].occupy("X"):
#                     return cell_number
#                 else:
#                     print("Cell is already occupied. Try again.")
#             else:
#                 print("Invalid input. Please enter a number between 1 and 9.")
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.board = Board()
#         self.player1 = player1
#         self.player2 = player2
#
#     def start_turn(self, player, symbol):
#         self.board.display()
#         print(f"{player.name}'s turn ({symbol}):")
#         cell_number = player.make_move(self.board)
#         if self.board.check_winner(symbol):
#             print(f"{player.name} wins!")
#             player.wins += 1
#             return True
#         return False
#
#     def start_game(self):
#         player_symbols = {"X": self.player1, "O": self.player2}
#         while True:
#             for symbol, player in player_symbols.items():
#                 if self.start_turn(player, symbol):
#                     return
#                 if all(cell.symbol != " " for cell in self.board.cells):
#                     print("It's a tie!")
#                     return
#                 print()
#             print(f"Score - {self.player1.name}: {self.player1.wins}, {self.player2.name}: {self.player2.wins}")
#             print("=" * 20)
#             play_again = input("Do you want to play again? (yes/no): ")
#             if play_again.lower() != "yes":
#                 return
#
#
# player1_name = input("Enter player 1 name: ")
# player2_name = input("Enter player 2 name: ")
# player1 = Player(player1_name)
# player2 = Player(player2_name)
# game = Game(player1, player2)
# game.start_game()
