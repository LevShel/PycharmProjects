# Задача 1. Скороговорка
# Дан текст вот такой английской скороговорки:
# How much wood would a woodchuck chuck if a woodchuck could chuck wood?
#
# С помощью модуля re реализуйте программу, которая выполняет следующие действия по порядку:
# Определить, начинается ли текст с шаблона wo.
# Найти первое упоминание шаблона wo в тексте.
# Определить содержимое найденной по шаблону подстроки из пункта 2.
# Найти позицию, с которого начинается первое упоминание шаблона wo.
# Найти позицию, на которой заканчивается первое упоминание шаблона wo.
# Получить список из каждого упоминания шаблона wo в тексте.
# Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».
# По каждому действию вывести соответствующий результат. Не используйте методы строк.
# Не забывайте использовать приписку r в шаблонах.
#
# Ожидаемый результат работы программы:
#
# Поиск шаблона в начале строки: None
# Поиск первого найденного совпадения по шаблону: <re.Match object; span=(9, 11), match='wo'>
# Содержимое найденной подстроки: wo
# Начальная позиция: 9
# Конечная позиция: 11
# Список всех упоминаний шаблона: ['wo', 'wo', 'wo', 'wo', 'wo']
# Текст после замены: How much ЗАМЕНАod ЗАМЕНАuld a ЗАМЕНАodchuck chuck if a ЗАМЕНАodchuck could chuck ЗАМЕНАod?

import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result_1 = re.match(r'wo', text)
result_2 = re.search(r'wo', text)
result_3 = result_2.group(0)
result_4 = result_2.start()
result_5 = result_2.end()
result_6 = re.findall(r'wo', text)
result_7 = re.sub(r'wo', 'ЗАМЕНА', text)

print('1. Поиск шаблона в начале строки:', result_1)
print('2. Поиск первого найденного совпадения по шаблону:', result_2)
print('3. Содержимое найденной подстроки:', result_3)
print('4. Начальная позиция:', result_4)
print('5. Конечная позиция:', result_5)
print('6. Список всех упоминаний шаблона:', result_6)
print('7. Текст после замены:', result_7)