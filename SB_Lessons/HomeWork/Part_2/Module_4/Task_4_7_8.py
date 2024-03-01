# Задание 8. Шифр Цезаря
# Что нужно сделать
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась
# на следующую по алфавиту через K позиций по кругу. Если взять русский алфавит и K,
# равное 3, то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д
# и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу, которая изменит
# фразу при помощи шифра Цезаря.
# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.

def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 26] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = ('abcdefghij'  # 1...10
            'klmnopqrst'  # 11...20
            'uvwxyz')  # 21...26

in_string = input('Your message: ')
k = int(input('k = '))

caesar = caesar_cipher(in_string, k)
print("Caesar's cipher: ", caesar)
