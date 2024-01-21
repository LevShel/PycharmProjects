# Шапка
print('\n\n+--------------+')
print('| Memory stick |')
print('+----- by ШелЛ +\n\n')

# Исходная заметка
array_of_memo = []
i = 1

# Описание комманд
command = ''
def memo_menu():
  print('M E N U\nYou can use:\nA. Add memo\nV. View memo\nD. Delete memo\nQ: quit\n')

# Цикл программы
while True:
  memo_menu()
  command = input("Выберите действие: ")

# Добавление заметки
  if command == 'A':
    while True:
      print('Введите ', i, ' запись (или введите "0" для завершения)')
      memo = input('> ')
      i += 1
      if memo.lower() == '0': # окончание добавления заметок
        i -= 1
        print('Ок! Заметки добавлены и сохранены.\n\n')
        break
      array_of_memo.append(memo)

# Просмотр заметки
  if command == 'V':
    print("Список Ваших заметок:")
    i = 1
    for memo in array_of_memo:
      print(i, end='. ')
      print(memo)
      i +=1

# Удаление заметки
  if command == 'D':
    i = input('Choose number of memo: ')
    memory = None
    print('Ok! Memo', i, 'was deleted.')

# Выход
  if command == 'Q':
    print('\n\nBye!\n')
    print('~~~~~~~~~~~~')
    input()
    break