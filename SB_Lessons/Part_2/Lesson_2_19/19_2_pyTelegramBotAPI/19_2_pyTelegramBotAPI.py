"""
Существует множество библиотек для разработки, но мы остановимся на pyTelegramBotAPI,
так как она довольно проста в использовании и имеет большое сообщество.
Для начала нужно создать самого бота с помощью BotFather
и получить у него токен — секретный ключ для оживления нашего виртуального помощника.
Простейший бот выглядит так:
"""
# from typing import Any
#
# import telebot
#
# bot = telebot.TeleBot('TOKEN')

"""
На команды /start и /help он ответит любимым приветствием.
А на всё остальное повторит то, что написал пользователь.
"""
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message: Any) -> None:
#     bot.reply_to(message, 'Hello, World!')

"""
Код `func=lambda message: True` означает, что любое сообщение обработается
с помощью обработчика сообщений echo_all.
Важно, чтобы он был объявлен после всех обработчиков. Функция func может быть более сложной,
например передавать, содержит ли сообщение какое-либо слово или было ли отправлено изображение.
"""
# @bot.message_handler(func=lambda message: True)
# def echo_all(message: Any) -> None:
#     bot.reply_to(message, message.text)


# if __name__ == '__main__':
#     bot.infinity_polling()

""" 
Для отправки сообщения используется команда send_message:
"""
# bot.send_message(message.chat.id, 'Новое сообщение!')

"""
Навигация
Возникает вопрос: что, если, помимо команд, пользователь должен вводить какие-то данные, 
с которыми впоследствии нужно что-то сделать? Здесь также есть два основных способа навигации.
1. register_next_step_handler
После обработки сообщения мы явно указываем следующий обработчик:
"""
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     mesg = bot.send_message(message.chat.id, 'Введите имя')
#     bot.register_next_step_handler(mesg, test)
#
#
# def test(message):
#     name = message.text
#     bot.send_message(message.chat.id, f'Ваше имя: {name}')


"""
2. Состояния
Этот способ работает по принципу автомата состояний: 
мы знаем, в каком состоянии сейчас находимся, но не знаем, как мы тут оказались.
В документации библиотеки приведён отличный пример. В классе MyStates мы указываем состояния, 
в которых можем оказаться (строка 31). С помощью декораторов обозначаем, 
какое состояние должно обрабатываться (строки 50, 58, 69, 80, 94) 
и куда необходимо перейти с помощью set_state (строка 45). 
Дополнительно нужно добавить StateFilter в качестве фильтра (строка 103) 
и инициализировать хранилище состояний (строка 24).
    Хранение данных
В том же примере реализовано хранение данных 
на основе контекстного менеджера retrieve_data, 
с помощью которого можно взаимодействовать с данными текущего пользователя (строки 65, 76, 85). 
Плюс в том, что нам не нужно использовать глобальные переменные 
и за нас заранее разграничили данные между пользователями, 
так что здесь можно безопасно хранить любую информацию.

https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_states.py
"""
# import telebot # telebot
#
# from telebot import custom_filters
# from telebot.handler_backends import State, StatesGroup #States
#
# # States storage
# from telebot.storage import StateMemoryStorage
#
#
# # Starting from version 4.4.0+, we support storages.
# # StateRedisStorage -> Redis-based storage.
# # StatePickleStorage -> Pickle-based storage.
# # For redis, you will need to install redis.
# # Pass host, db, password, or anything else,
# # if you need to change config for redis.
# # Pickle requires path. Default path is in folder .state-saves.
# # If you were using older version of pytba for pickle,
# # you need to migrate from old pickle to new by using
# # StatePickleStorage().convert_old_to_new()
#
#
#
# # Now, you can pass storage to bot.
# state_storage = StateMemoryStorage() # you can init here another storage
#
# bot = telebot.TeleBot("TOKEN",
# state_storage=state_storage)
#
#
# # States group.
# class MyStates(StatesGroup):
#     # Just name variables differently
#     name = State() # creating instances of State class is enough from now
#     surname = State()
#     age = State()
#
#
#
#
# @bot.message_handler(commands=['start'])
# def start_ex(message):
#     """
#     Start command. Here we are starting state
#     """
#     bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
#     bot.send_message(message.chat.id, 'Hi, write me a name')
#
#
# # Any state
# @bot.message_handler(state="*", commands=['cancel'])
# def any_state(message):
#     """
#     Cancel state
#     """
#     bot.send_message(message.chat.id, "Your state was cancelled.")
#     bot.delete_state(message.from_user.id, message.chat.id)
#
# @bot.message_handler(state=MyStates.name)
# def name_get(message):
#     """
#     State 1. Will process when user's state is MyStates.name.
#     """
#     bot.send_message(message.chat.id, 'Now write me a surname')
#     bot.set_state(message.from_user.id, MyStates.surname, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['name'] = message.text
#
#
# @bot.message_handler(state=MyStates.surname)
# def ask_age(message):
#     """
#     State 2. Will process when user's state is MyStates.surname.
#     """
#     bot.send_message(message.chat.id, "What is your age?")
#     bot.set_state(message.from_user.id, MyStates.age, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['surname'] = message.text
#
# # result
# @bot.message_handler(state=MyStates.age, is_digit=True)
# def ready_for_answer(message):
#     """
#     State 3. Will process when user's state is MyStates.age.
#     """
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         msg = ("Ready, take a look:\n<b>"
#                f"Name: {data['name']}\n"
#                f"Surname: {data['surname']}\n"
#                f"Age: {message.text}</b>")
#         bot.send_message(message.chat.id, msg, parse_mode="html")
#     bot.delete_state(message.from_user.id, message.chat.id)
#
# #incorrect number
# @bot.message_handler(state=MyStates.age, is_digit=False)
# def age_incorrect(message):
#     """
#     Wrong response for MyStates.age
#     """
#     bot.send_message(message.chat.id, 'Looks like you are submitting a string in the field age. Please enter a number')
#
# # register filters
#
# bot.add_custom_filter(custom_filters.StateFilter(bot))
# bot.add_custom_filter(custom_filters.IsDigitFilter())
#
# bot.infinity_polling(skip_pending=True)
