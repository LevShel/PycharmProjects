# Задание 8. Снова палиндром
# Что нужно сделать
# Пользователь вводит строку. Необходимо написать программу, которая определяет,
# существует ли у этой строки перестановка, при которой она станет палиндромом.
# Затем она должна выводить соответствующее сообщение.
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом

str_input = input('>: ')
dict_syms = {}
for sym in str_input:
    if int(str_input.count(sym)) not in dict_syms:
        dict_syms[int(str_input.count(sym))] = [sym]
    else:
        dict_syms[int(str_input.count(sym))].append(sym)

odd_count = sum(1 for key in dict_syms.keys() if key % 2 != 0)
odd_key = []
for key in dict_syms.keys():
    if key % 2 != 0:
        odd_key.append(key)

print(dict_syms)
print('odd_count: ', odd_count)
print('odd_key: ', odd_key)
print('len(dict_syms[odd_key[0]]):', len(dict_syms[odd_key[0]]))

if (odd_count <= 1 and
        len(odd_key) <= 1 and
        len(dict_syms[odd_key[0]]) % 2 != 0):
    print('May be a palindrome.')
else:
    print('Impossible make a palindrome.')

# Мой коммент:
# возможно, лучше в качестве ключей брать буквы,
# а в качестве значений - их количество.
# Тогда можно будет просто считать количество нечётных значений,
# и, если нечётных значений > 1, то палиндром получить нельзя.
