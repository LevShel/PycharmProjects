# Задача 1. Работа с файлом 2
# Что нужно сделать
# Реализуйте модернизированную версию контекст-менеджера File:
# теперь при попытке открыть несуществующий файл менеджер должен автоматически создавать
# и открывать этот файл в режиме записи;
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.

import os


class File:
    def __init__(self, filename: str, operation: str) -> None:
        self.filename = filename
        self.operation = operation
        self.text = None

    def write(self, text: str) -> None:
        self.text = text
        with open(self.filename, self.operation, encoding='utf-8') as some_file:
            some_file.write(text)

    def read(self) -> None:
        with open(self.filename, self.operation, encoding='utf-8') as some_file:
            text = some_file.readline()
        return print(text)

    def create(self) -> 'File':
        with open(self.filename, 'a', encoding='utf-8'):
            pass
        return self

    def __enter__(self) -> 'File':
        if not os.path.exists(self.filename):
            self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type:
            print(f'Тип ошибки: {exc_type}\n'
                  f'Значение ошибки: {exc_val}\n'
                  f'"След" ошибки: {exc_tb}')
        return True


with File('example.txt', 'r') as file:
    file.read()

with File('example_2.txt', 'w') as file:
    file.write('Всем привет!')

with File('example_2.txt', 'r') as file:
    file.read()
