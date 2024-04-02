class Person:
    """
    Базовый класс, описывающий человека

    __count (int): общее количество человек

    Args:
        name (str): передаётся имя человека
        age (int): передаётся возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов (экземпляров)
    """
    __count = 0
    max_count = 5

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f'Name: {self.__name}\tAge: {self.__age}'

    def get_count(self):
        return self.__count

    def get_age(self):
        """
        Геттер для получения возраста.

        :return: __age
        :rtype: int
        """
        return self.__age

    def set_age(self, age):
        """
        Сеттер для установления возраста.

        :param age: возраст
        :type: int
        :raise Exception: если возраст не в границах от 1 до 90, то вызывается исключение
        """
        if age in range(1, 90):
            self.__age = age
            return self.__age
        else:
            raise Exception('Wrong age.')


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        return '\n'.join((info, f'Student study in {self.university}'))


class Employee(Person):
    """
    Класс Работник. Родитель: Person.

    Args:
        name (str): передаётся имя человека
        age (int): передаётся возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
        company (str): должность работника
        salary (str): зарплата работника
    """
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        return '\n'.join((info, f'Employer works in {self.company} and have salary {self.salary}'.encode()))


student = Student(name='Lev', age=30, university='BMSTU')
employer = Employee(name='Lev', age=30, salary=300000, company='Yandex')
print(student)
print(employer)
