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


class Date:

    @classmethod
    def from_string(cls, input_date: str) -> str:
        """
        Преобразует строку в формате "день-месяц-год" в объект даты.
        Args:
            input_date (str): Строка, представляющая дату в формате "день-месяц-год".
        Returns:
            str: Строковое представление даты в виде "День: <day> Месяц: <month> Год: <year>",
            если дата корректна, иначе 'False'.
        """
        day, month, year = map(int, input_date.split('-'))
        if Date.is_date_valid(input_date):
            return f'День: {day}\tМесяц: {month}\tГод: {year}'
        else:
            return 'False'

    @classmethod
    def is_date_valid(cls, input_date: str) -> bool:
        """
        Проверяет корректность даты.
        Args:
            input_date (str): Строка, представляющая дату в формате "день-месяц-год".
        Returns:
            bool: True, если дата корректна, иначе False.
        """
        day, month, year = map(int, input_date.split('-'))
        if ((1 <= int(day) <= 31) and
                (1 <= int(month) <= 12) and
                (int(year) > 0)):
            return True
        else:
            return False


my_date = Date.from_string('10-12-2077')
print(my_date)  # День: 10 Месяц: 12 Год: 2077
print(Date.is_date_valid('10-12-2077'))  # True
print(Date.is_date_valid('40-12-2077'))  # False
