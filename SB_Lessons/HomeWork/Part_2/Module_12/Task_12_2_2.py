# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять
# только из букв) и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса
# считается общее количество инициализированных объектов. Реализуйте сокрытие данных
# для всех атрибутов (как статических, так и динамических), а для изменения и получения
# данных объекта напишите специальные геттеры и сеттеры.
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в уроке.

class Human:
    __count = 0

    def __init__(self, name=None, age=None):
        self.__name = name if name else 'Noname'
        self.__age = age if age else 0
        Human.__count += 1

    def set_name(self, name):
        if isinstance(name, str):
            sym = True
            for sym in name:
                if sym.isalpha():
                    pass
                else:
                    print('Wrong name. Use letters only.')
                    sym = False
                    break
            if sym:
                self.__name = name
                return self.__name
        else:
            raise Exception('Wrong name. Name must be a string.')

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
            return self.__age
        else:
            raise Exception('Wrong age. Age must be 0...100.')

    def get_count(self):
        return self.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'{self.__name}\t{self.__age}'


first_person = Human()
print(first_person.get_count(), first_person.__str__())
second_person = Human()
print(second_person.get_count(), second_person.__str__())
# first_person.set_name('Lev_16')
# print(first_person.get_name())
first_person.set_name('Lev')
print(first_person.get_name())
# first_person.set_age(150)
# print(first_person.get_age())
first_person.set_age(30)
print(first_person.get_age())
print(first_person.__str__())