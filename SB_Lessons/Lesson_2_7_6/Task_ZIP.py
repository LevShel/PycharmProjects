# Исходные списки
names = ['Tom', 'Bob', 'Albert']
ages = [20, 33, 55]

# Соединение списка функцией zip
info = zip(names, ages)
print(info) # Зашифрованный результат
print()
# Распаковка zip
for i_person in info:
    print(i_person, end=' ') # Читаемый результат
print()
print()

# Преобразование в список
info = list(zip(names, ages))
print(info)
print()

# Преобразование в словарь
info = dict(zip(names, ages))
print(info)
print()

# Упаковка в словарь с изменением данных (+10 к age)
info = {
    i_name: i_age +10
    for i_name, i_age in zip(names, ages)
}
print(info)