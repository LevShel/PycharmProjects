class Person:
    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.__age = age
        self.__friends = friends

    def __str__(self) -> str:
        return f'Name: {self.__name}\tAge: {self.__age}\nFriends: {self.__friends}'

    def set_age(self, age: int) -> None:
        self.__age = age

    def get_age(self) -> int:
        return self.__age
    