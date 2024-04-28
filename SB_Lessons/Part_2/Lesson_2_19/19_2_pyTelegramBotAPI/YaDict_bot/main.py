import json
import telebot
from telebot.types import Message
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

import api
from config import BOT_TOKEN, DEFAULT_LANG
from states import States

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

available_langs = api.get_langs()


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'Привет! Я бот Яндекс.Словаря. Я умею переводить слова и подбирать синонимы.\n\n'
        f'- /set_lang. Выбрать направление перевода [{DEFAULT_LANG}]\n'
        '- /lookup. Перевести слово или фразу'
    )
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['set_lang'])
def set_lang_command(message: Message) -> None:
    lang_list = ', '.join(available_langs)
    bot.send_message(message.chat.id, f'Выберите один из представленных направлений перевода:\n\n{lang_list}')
    bot.set_state(message.from_user.id, States.lang, message.chat.id)


@bot.message_handler(state=States.lang)
def set_lang(message: Message) -> None:
    chosen_lang = message.text
    if chosen_lang not in available_langs:
        bot.send_message(message.chat.id, 'Такого направления перевода нет. Попробуйте еще раз')
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['lang'] = message.text
        bot.send_message(message.chat.id, f'Выбрано направление {data["lang"]}')

    bot.send_message(message.chat.id, "Для поиска напишите /lookup")
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['lookup'])
def lookup_command(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'Введите текст или фразу для поиска.\n'
        'Для смены направления напишите /set_lang'
    )
    bot.set_state(message.from_user.id, States.lookup, message.chat.id)


@bot.message_handler(state=States.lookup)
def lookup(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = api.lookup(text=message.text, lang=data.get('lang', DEFAULT_LANG))
        json_raw = json.dumps(result, ensure_ascii=False, indent=2)
        bot.send_message(message.chat.id, f'<pre>{json_raw}</pre>', parse_mode='html')
    bot.send_message(message.chat.id, 'Введите текст или фразу для поиска')


if __name__ == '__main__':
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands([
        telebot.types.BotCommand("set_lang", "Сменить направление перевода"),
        telebot.types.BotCommand("lookup", "Поиск слова или фразы"),
    ])
    bot.polling()
