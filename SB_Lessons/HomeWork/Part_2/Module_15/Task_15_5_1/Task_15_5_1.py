# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами. Он должен принимать на вход имя файла
# и режим чтения/записи и открывать сам файл. В начале работы менеджер возвращает файловый объект,
# а в конце — закрывает файл.
#
# Пример основного кода:
# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)

class File:
    def __init__(self, filename: str, operation: str) -> None:
        self.filename = filename
        self.operation = operation
        self.text = None

    def __enter__(self) -> 'File':
        open(self.filename, self.operation)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return True

    def write(self, text: str) -> None:
        self.text = text
        with open(self.filename, self.operation, encoding='utf-8') as some_file:
            some_file.write(text)

    def read(self) -> None:
        with open(self.filename, self.operation, encoding='utf-8') as some_file:
            text = some_file.readline()
        return print(text)


with File('example.txt', 'r') as file:
    file.read()  # ('Всем привет!')
