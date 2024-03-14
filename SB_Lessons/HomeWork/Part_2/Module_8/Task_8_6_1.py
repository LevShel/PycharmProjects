# Задача 1. Работа с файлом
# Вы пишете небольшое приложение для работы с файлами. Реализуйте функцию,
# которая может принимать на вход три аргумента: вопрос пользователю (на который нужно
# ответить да или нет), сообщение о неправильном вводе и количество попыток.
# Вопрос — обязательный позиционный аргумент, остальные — со значениями по умолчанию.
# При корректном ответе функция может возвращать что угодно — например,
# число 1 при ответе «да» или 0 при ответе «нет».
# В основной программе вызовите функцию минимум три раза: только с вопросом,
# с вопросом и сообщением об ошибке, с вопросом и количеством попыток.
#
# Пример работы программы:
# Вы действительно хотите выйти? что
# Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
# Осталось попыток: 3
# Вы действительно хотите выйти? да
# Удалить файл? не знаю
# Так удалить или нет?
# Осталось попыток: 3
# Удалить файл? нет
# Записать файл? ага
# Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
# Осталось попыток: 1
# Записать файл? да

def ask_user(question,
             compliant='Wrong answer. Please type "Yes" or "No"',
             retries=4):
    while True:
        answer = input(question).lower()
        if answer == 'yes':
            return 1
        if answer == 'no':
            return 0
        retries -= 1
        if retries == 0:
            print('There is no retries.')
            break
        print(compliant)
        print(f'You have {retries} retries.')


ask_user('You want exit?\n'
         '>: ')
ask_user('Delete file?\n'
         '>: ',
         compliant='So, delete or not?')
ask_user('Save file?\n'
         '>: ',
         retries=2)