# Задача 5. Часы
# Что нужно сделать
# Напишите программу, которая получает на вход число n (количество минут), затем считает,
# сколько это будет в часах и сколько минут останется, и выводит на экран эти два результата.

minutes = int(input('How much minutes: '))

hours = minutes / 60
rem_minutes = minutes % 60

print(f'In {minutes} is {hours} hours.')
print(f'There are {rem_minutes} remains.')