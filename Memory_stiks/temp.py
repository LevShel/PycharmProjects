# Куски кода для вставки

# Создание массива строк с неизвестным количеством строк
array_of_memo = []
i = 1
while True:
  print('Введите ',i, ' строку (или введите "0" для завершения)')
  memo = input('> ')
  i +=1
  print()

  if memo.lower() == '0':
      break

  array_of_memo.append(memo)

# Вывод элементов массива
print("Массив строк:")
for memo in array_of_memo:
  print(memo)
  print()

# Вывод определённой строки массива
i = int(input('Введите номер строки для вывода: '))
print(array_of_memo[i-1])