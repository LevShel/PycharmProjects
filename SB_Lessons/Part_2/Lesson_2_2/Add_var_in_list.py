# Начальный пустой список
spisok = []

# Количество добавляемых позиций
q = int(input('Enter quantity of nums: '))

# Ввод новых позиций и добавление их в список
for _ in range(q):
    input_num = input('Enter num: ')
    spisok.append(input_num)
# Вывод списка
for num in spisok:
    print(num, end = ' ')