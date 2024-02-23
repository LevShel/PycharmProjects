# Задача 6. Ход конём
# Что нужно сделать
# В рамках разработки шахматного ИИ стоит новая задача: по заданным вещественным
# координатам коня и точки программа должна определить, может ли конь ходить в эту точку.
# Используйте как можно меньше конструкций if и логических операторов. Обеспечьте контроль
# ввода.
# Пример:
# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

print('Введите местоположение коня:')
horse_x = float(input('x = '))
horse_y = float(input('y = '))
print('Введите местоположение точки на доске:')
dot_x = float(input('x = '))
dot_y = float(input('y = '))

# horse_x = int(round(horse_x, 1) * 10)
horse_xx = math.floor(horse_x)
horse_x = int((horse_x - horse_xx) * 10)
# horse_y = int(round(horse_y, 1) * 10)
horse_yy = math.floor(horse_y)
horse_y = int((horse_y - horse_yy) * 10)
# dot_x = int(round(dot_x, 1) * 10)
dot_xx = math.floor(dot_x)
dot_x = int((dot_x - dot_xx) * 10)
# dot_y = int(round(dot_y, 1) * 10)
dot_yy = math.floor(dot_y)
dot_y = int((dot_y - dot_yy) * 10)
print(f'Конь в клетке ({horse_x}, {horse_y}). Точка в клетке ({dot_x}, {dot_y}).')

# if (dot_x == horse_x + 1) and (dot_y == horse_y + 2):
#     print('Да, конь может ходить в эту точку.')
# elif (dot_x == horse_x + 2) and (dot_y == horse_y + 1):
#     print('Да, конь может ходить в эту точку.')
# elif (dot_x == horse_x + 2) and (dot_y == horse_y - 1):
#     print('Да, конь может ходить в эту точку.')
# elif (dot_x == horse_x + 1) and (dot_y == horse_y - 2):
#     print('Да, конь может ходить в эту точку.')
# else:
#     print('Нет, конь не может ходить в эту точку.')
if (math.fabs(dot_x - horse_x) == 1) and (math.fabs(dot_y - horse_y) == 2):
    print('Да, конь может ходить в эту точку.')
elif (math.fabs(dot_x - horse_x) == 2) and (math.fabs(dot_y - horse_y) == 1):
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')