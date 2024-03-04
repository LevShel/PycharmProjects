# Задание 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать пароль. Этот пароль должен
# состоять минимум из восьми символов, содержать хотя бы одну большую букву и не менее
# трёх цифр. Тогда он будет считаться надёжным.
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока
# этот пароль не станет надёжным. Должна использоваться латиница.
# Пример
# Придумайте пароль: qwerty.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123.
# Это надёжный пароль.

def count_special_symbols(inp_str):
    special_symbols = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
    if any(sym in inp_str for sym in special_symbols):
        return True
    else:
        return False


def count_nums(inp_str):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    for sym in inp_str:
        if sym in nums:
            i += 1
    return i


def count_uppercase(inp_str):
    return any(sym.isupper() for sym in inp_str)


pwd = input('\nCOME UP WITH A PASSWORD\n'
            '! The password must consist of at least eight characters,\n'
            'contain at least one large letter, one special character\n'
            'and at least three digits.\n'
            '>: ')
if (len(pwd) > 8 and
        count_special_symbols(pwd) and
        count_nums(pwd) >= 3 and
        count_uppercase(pwd)):
    print('True password.')
else:
    print('Wrong password.')
