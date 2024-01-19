# Шапка
print('+--------------+')
print('| Memory stick |')
print('+----- by ШелЛ +')
print()

# Исходная заметка
array_of_memo = []
i = 1

# Описание комманд
print('You can use:')
print('A. Add memo')
print('V. View memo')
print('D. Delete memo')
print('Q: quit')
print()

# Цикл программы
while True:
  command = input("Command: ")

  # Добавление заметки
  if command == 'A':
    """
    memory =input('What you want to add? ')
    print('Ok! Memo was added.')
    print()
    """

    while True:
      print('Введите ', i, ' строку (или введите "0" для завершения)')
      memo = input('> ')
      i += 1
      print()

      if memo.lower() == '0':
        i -= 1
        break

      array_of_memo.append(memo)

  # Просмотр заметки
  if command == 'V':
    """
    print(memory)
    print()
    """
    print("Массив строк:")
    for memo in array_of_memo:
      print(memo)
      print()

  # Удаление заметки
  if command == 'D':
    i = input('Choose number of memo: ')
    memory = None
    print('Ok! Memo', i, 'was deleted.')
    print()

  # Выход
  if command == 'Q':
    print('Bye!')
    print()
    print('~~~~~~~~~~~~')
    break