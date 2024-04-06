class Person:
    __count = 0  # HIDDEN DATA

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return (f'Name: {self.__name},\n'
                f'Age: {self.__age}\n')

    def get_count(self):  # GETTER
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age):  # SETTER
        if age in range(1, 90):
            self.__age = age
            return self.__age
        else:
            raise Exception('Wrong age.')


misha = Person('Misha', 20)
print('get_count(): ', misha.get_count())
tom = Person('Tom', 25)
print('get_count(): ', misha.get_count())
print('get_age(): ', tom.get_age())
tom.set_age(30)
print('get_age(): ', tom.get_age())

print('__str__():\n', misha.__str__())
