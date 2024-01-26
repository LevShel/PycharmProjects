# Шапка
name_of_programm = 'BMI calculator'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')

# Ввод исходных данных
age = int(input('Enter the age (y.o.): '))
height = float(input('Enter the height (cm): '))
weight = float(input('Enter the weight (kg): '))

# Расчёт ИМТ по формуле
BMI = round((weight) / ((height / 100) ** 2), 2)

# Вывод результата расчёта
print('\nYour BMI = ', BMI, '\n')

# Заключение
if BMI < 18.5:
    print('You are SHORTAGE')
elif 18.5 <= BMI < 25:
    print('You are STANDART')
elif 25 <= BMI < 30:
    print('You are EXCESS')
else:
    print('You are FATNESS')
