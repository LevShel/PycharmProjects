# Задача 3. Рыбалка
# Наши прекрасные родственники удачно сходили на рыбалку.
# Настолько, что ходили мешком перетаскивать рыбу с берега в машину целых n раз.
# Каждый мешок они взвешивали на электронных весах (все мешки весили по-разному).
# Напишите программу для весов, которая считает суммарный вес мешков и выводит его на экран.

n = int(input('How many times went to drag fish from the shore to the car? '))

i = 0
total_weight = 0

while i != n:
    i += 1
    weight = float(input(f'How much does the {i} bag weight? '))
    total_weight += weight

print('Total weight is: ', total_weight)