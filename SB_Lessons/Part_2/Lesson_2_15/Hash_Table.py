"""
Пример простой реализации хеш-таблицы на Python
"""


class HashTable:
    def __init__(self):
        self.size = 10  # Размер хеш-таблицы
        self.table = [None] * self.size  # Инициализация массива с None

    def _hash_function(self, key):
        return hash(key) % self.size  # Хеш-функция, преобразующая ключ в индекс

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index] = value  # Вставка значения по соответствующему индексу

    def get(self, key):
        index = self._hash_function(key)
        return self.table[index]  # Получение значения по ключу

    def remove(self, key):
        index = self._hash_function(key)
        self.table[index] = None  # Удаление значения по ключу


"""
Модуль hashlib
Этот модуль является частью стандартной библиотеки Python и предоставляет интерфейс для различных хеш-функций, 
таких как MD5, SHA-1, SHA-256. Он позволяет вычислять хеш-значение для произвольных данных, например строк или 
байтовых объектов.
Пример использования модуля hashlib для вычисления хеш-значения строки с использованием SHA-256:
"""
# import hashlib
# data = "Hello, World!"
# hash_object = hashlib.sha256(data.encode())
# hex_digest = hash_object.hexdigest()
# print(hex_digest) # Выводит хеш-значение SHA-256


"""
Библиотека mmh3
Эта библиотека предоставляет реализацию MurmurHash — быстрого и эффективного некриптографического хеш-алгоритма. 
Обычно он используется для хеширования данных в контексте поиска, индексации или фильтрации.
Пример использования библиотеки mmh3 для вычисления хеш-значения строки:
"""
# import mmh3
# data = "Hello, World!"
# hash_value = mmh3.hash(data)
# print(hash_value)  # Выводит хеш-значение MurmurHash


"""
Библиотека pyhash
Эта библиотека предоставляет широкий выбор хеш-функций, включая CRC, CityHash, FarmHash, SpookyHash и другие. 
Она обеспечивает гибкость выбора хеш-функции в зависимости от конкретных потребностей.
Пример использования библиотеки pyhash для вычисления CRC32 хеш-значения строки:
"""
# import pyhash
# data = "Hello, World!"
# crc32_hasher = pyhash.crc32()
# hash_value = crc32_hasher(data)
# print(hash_value)  # Выводит хеш-значение CRC32
