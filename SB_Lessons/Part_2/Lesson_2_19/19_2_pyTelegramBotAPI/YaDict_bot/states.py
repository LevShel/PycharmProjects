from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    base = State()
    lang = State()
    lookup = State()
