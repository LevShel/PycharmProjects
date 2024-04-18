# Задача 3. Дата
# Что нужно сделать
# Реализуйте класс Date, который должен:
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений
# дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
# При тестировании программы объект класса Date должен инициализироваться исключительно через метод
# конвертации, например:
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
# Пример основного кода:
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False

from abc import abstractmethod


class Date:

    @abstractmethod
    def from_string(date: str) -> str:
        pass
    # TODO

    @abstractmethod
    def is_date_valid(date: str) -> bool:
        pass
    # TODO


date = Date.from_string('10-12-2077')
print(date)  # День: 10 Месяц: 12 Год: 2077
print(Date.is_date_valid('10-12-2077'))  # True
print(Date.is_date_valid('40-12-2077'))  # False
