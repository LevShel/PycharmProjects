# Исходные данные
true_login = 'admin'
true_password = 'admin'
attempts = 3
input_login = None
input_password = None

# Начало цикла входа
while (attempts > 0) and ((input_login != true_login) or (input_password != true_password)):

    # Ввод логина/пароля
    input_login = input('Username: ')
    input_password = input('Password: ')
    attempts -= 1

    # Ошибка. Осталось ? попыток
    if attempts > 0 and ((input_login != true_login) or (input_password != true_password)):
        print('Error! Incorrect username or password. Try again.')
        print('There are', attempts, 'attempts left!')

    # Попыток больше нет
    if attempts == 0 and ((input_login != true_login) or (input_password != true_password)):
        print('You have no more attempts! Try later.')
        break

    # Логин/пароль правильный. Успешный вход
    if (input_login == true_login) and (input_password == true_password):
        print('You login succesfully! Enjoy :)')