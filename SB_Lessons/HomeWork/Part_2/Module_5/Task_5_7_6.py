# Задание 6. Сжатие
# Что нужно сделать
# Из-за того, что объём данных увеличился, понадобилось сжать эти данные, но так,
# чтобы не потерять важную информацию. Для этого было придумано специальное кодирование:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'. То есть группы одинаковых символов исходной
# строки заменяются на эти символы и количество их повторений в строке.
# Напишите программу, которая считывает строку, кодирует её, используя предложенный
# алгоритм, и выводит закодированную последовательность на экран. Код должен учитывать
# регистр символов.
# Пример
# Введите строку: aaAAbbсaaaA.
# Закодированная строка: a2A2b2с1a3A1.


#           === MY VARIANT (not correct) ===
word = input('>: ')
cipher = []
rep = 1
letters = [sym for sym in word]
for sym in range(len(letters)-1):
    if letters[sym] == letters[sym+1]:
        cipher.append(letters[sym])
        rep += 1
    else:
        cipher.append(rep)
        cipher.append(sym)
        rep = 1
for _ in cipher:
    print(_, end='')


#           === CHAT GPT ===
# def encode_string(s):
#     encoded = ''
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             encoded += s[i - 1] + str(count)
#             count = 1
#     encoded += s[-1] + str(count)  # Обработка последнего символа
#     return encoded
#
#
# # Считываем строку от пользователя
# s = input("Введите строку: ")
#
# # Кодируем строку и выводим результат
# encoded_string = encode_string(s)
# print("Закодированная строка:", encoded_string)
