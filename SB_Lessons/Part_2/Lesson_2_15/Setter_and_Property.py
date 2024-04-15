class Person:
    """
    Человек
    Args:
        name (str): имя
        age (int): возраст
    Attributes:
        _name (str): имя
        _age (int): возраст (от 1 до 100, иначе ошибка)
    """

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f'Name: {self._name}\tAge: {self._age}'

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @age.setter
    def age(self, age: int) -> None:
        if age in range(1, 100):
            self._age = age
        else:
            raise Exception('Wrong age!')


my_person = Person(name='Lev', age=30)
print(my_person)
print(my_person.age)
my_person.age = 32
print(my_person.age)
print(my_person)
