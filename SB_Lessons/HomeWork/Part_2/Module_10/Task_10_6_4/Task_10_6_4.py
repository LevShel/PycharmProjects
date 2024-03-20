# Задача 4. Чат
# Что нужно сделать
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программу, которая может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1.	Посмотреть текущий текст чата.
# 2.	Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
# Примечание: для решения задачи вам достаточно текущих знаний, нужно лишь проявить
# немного фантазии и хитрости. Не углубляйтесь в дебри работы с сетями,
# создание GUI-приложений и прочее. Однако, если очень хочется, то останавливать вас никто
# не будет!

user_name = input('Enter your username: ')
print('Command list:\n'
      '1. Read\n'
      '2. New message\n')
while True:
    response = input('1/2 >: ')
    if response == '1':
        try:
            with open('chat_history.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('History not found.\n')
    elif response == '2':
        new_message = input(f'{user_name}: ')
        with open('chat_history.txt', 'a') as file:
            file.write(f'{user_name}: {new_message}\n')
    else:
        print('Wrong command.\n')
