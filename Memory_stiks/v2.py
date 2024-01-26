# Шапка
name_of_programm = 'MemorySticks'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')
# Исходная заметка
array_of_memo = []
i = 1

# Описание комманд
command = ''
# Меню
def memo_menu():
  print('\nM E N U\nYou can use:\nA. Add notes\nV. View notes\nD. Delete note\nQ: Quit\n')

# Цикл программы
while True:
  memo_menu()
  command = input("Select an action: ")

# Добавление заметки
  if command == 'A' or command == 'a':
    while True:
      print('Enter the ', i, ' entry (or enter "0" to complete):')
      memo = input('> ')
      i += 1
      if memo.lower() == '0':  # окончание добавления заметок
        i -= 1
        print('\nOk! Notes have been added and saved.\n\n')
        break
      array_of_memo.append(memo)

# Просмотр заметки
  if command == 'V' or command == 'v':
    print("A list of your notes:")
    i = 1
    for memo in array_of_memo:
      print(i, end='. ')
      print(memo)
      i +=1

# Удаление заметки
  if command == 'D' or command == 'd':
    i = int(input('Choose number of note to delete: '))
    del array_of_memo[i-1]
    print('Ok! Memo', i, 'was deleted.')

# Выход
  if command == 'Q' or command == 'q':
    print('\n\nThe work with the notes is completed! To close the window, press any key.\n')
    print('~~~~~~~~~~~~')
    input()
    break