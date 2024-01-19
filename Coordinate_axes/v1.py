# Ввод исходных размеров осей
height = int(input('Enter height: '))
width = int(input('Enter width: '))
print()

# Проверка на чётность
if (height % 2 != 0) or (width % 2 != 0):
  print('Error! Enter even numbers.')

# Отрисовка осей
else:
  for row in range(height):
    for col in range (width):
      if row == (height-2)/2:
        print('-', end = '')
        if col == (width-4)/2:
          print('+', end = '')
      elif col == (width-2)/2:
        print('|', end = '')
      else:
        print(' ', end = '')
    print()