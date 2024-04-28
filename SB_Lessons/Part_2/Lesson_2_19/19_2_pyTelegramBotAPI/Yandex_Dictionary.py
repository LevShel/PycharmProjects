"""
Яндекс предоставляет огромное количество API (https://yandex.ru/dev/), которые вы можете использовать в своих проектах.
Также существуют агрегаторы API от сервисов, например Public APIs (https://publicapis.dev/),
так что всегда можно найти подходящий вариант.
Получаем API-ключ
Попробуем повзаимодействовать с одним из них. Возьмём API «Яндекс Словаря». Для начала нужно получить бесплатный ключ
на странице сервиса (https://yandex.ru/dev/dictionary/).
Делаем пробные запросы
В документации есть два эндпоинта — ссылки, по которым можно обратиться за данными: getLangs и lookup.
Там же можно посмотреть примеры запросов.
Перейдя по ссылке ниже, вы можете увидеть JSON со списком доступных направлений перевода:
https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key=ВАШ_API_КЛЮЧ
Посмотрим, что с этим можно сделать в методе lookup. Здесь необходимо вводить дополнительные параметры:
направление перевода и текст. Также есть необязательные: язык интерфейса и опции поиска.
Возьмём слово «задача» и направление ru-en. Вставим их в URL-параметры:
https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=ВАШ_API_КЛЮЧ&lang=ru-en&text=задача
В ответ получим различные переводы и синонимы. Проделайте то же самое у себя в браузере.
Делаем запросы с помощью requests.
Сделаем то же самое, только с помощью Python.
"""

from pprint import pprint
import requests

API_KEY = 'dict.1.1.20240428T171652Z.d5ad14cd9aec6d4d.28143ffcf0a4e13ba66adea2cb224328990bb938'
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'


def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response


def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response


langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список направлений перевода')
    exit(1)

langs = langs_response.json()
print('Выберите одно из доступных направлений перевода')
print(langs)
while (lang := input('Введите направление: ')) not in langs:
    print('Такого направления нет. Попробуйте ещё раз')

text = input('Введите слово или фразу для перевода: ')
lookup_response = lookup(lang, text)
if lookup_response.status_code != 200:
    print('Не удалось выполнить перевод:', lookup_response.text)
    exit(1)

pprint(lookup_response.json())

"""
На что стоит обратить внимание
    * BASE_URL — часть ссылки, которая не меняется при обращениях к этому API.
    * Запрос делается с помощью requests.get, где первый аргумент — это ссылка, 
        а дальше мы указываем URL-параметры, передав их в params.p
В сырой ссылке URL-параметры выглядят так:
?key=ВАШ_API_КЛЮЧ&lang=ru-en&text=задача
В принципе, если вставить их в код таким образом, он всё равно сработает.
В виде словаря код выглядит так:
params = {
    'key': 'ВАШ_API_КЛЮЧ', 
    'lang': 'ru-en', 
    'text': 'задача'
}
Использование словаря повысит читаемость кода, поэтому этот способ предпочтительный.
    * Ещё есть requests.post, который посылает POST-запрос.
        Если GET-запрос предназначен для получения информации от сервера, 
        то POST — больше для передачи информации серверу. 
        Применяйте тот или иной метод в зависимости от документации.
    * Методы requests.get и requests.post возвращают объект ответа, 
        который содержит в себе код (2xx — успешные запросы, 4xx — неправильные запросы, 5xx — ошибки сервера), 
        а также текст. Если обращаемся в формате JSON, можно сразу получить его с помощью response.json().
В API некоторые данные могут передаваться в заголовках или теле запроса:
requests.post(url, headers={}, data={})
Часто в API указывают ключ в заголовке:
requests.post(url, headers={
    'X-RapidAPI-Key': 'ВАШ_API_КЛЮЧ',
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
}, data={
    'currency': 'USD'
})
У всех API разный контракт взаимодействия, поэтому тщательно изучайте документацию.
"""