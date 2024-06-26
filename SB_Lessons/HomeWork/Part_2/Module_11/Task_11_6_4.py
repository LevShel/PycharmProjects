# Задача 4. Магия
# Что нужно сделать
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов
# получается новый. У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
# Таблица преобразований:
# •	Вода + Воздух = Шторм;
# •	Вода + Огонь = Пар;
# •	Вода + Земля = Грязь;
# •	Воздух + Огонь = Молния;
# •	Воздух + Земля = Пыль;
# •	Огонь + Земля = Лава.
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо
# организовать как отдельный класс. Если результат не определён, то возвращается None.
# Примечание: сложение объектов можно реализовывать через магический метод __add__,
# вот пример использования:
# class ExampleOne:
#     def __add__(self, other):
#         return ExampleTwo()
# class ExampleTwo:
#     answer = 'сложили два класса и вывели'
# first_example = ExampleOne()
# second_example = ExampleTwo()
# result = first_example + second_example
# print(result.answer)
# Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие
# с остальными.

class Water:
    # •	Вода + Воздух = Шторм;
    # •	Вода + Огонь = Пар;
    # •	Вода + Земля = Грязь;
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None


class Air:
    # •	Воздух + Огонь = Молния;
    # •	Воздух + Земля = Пыль;
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    # •	Огонь + Земля = Лава.
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:
    pass


class Storm:  # Water + Air
    def __str__(self):
        return 'storm'


class Steam:  # Water + Fire
    def __str__(self):
        return 'steam'


class Mud:  # Water + Earth
    def __str__(self):
        return 'mud'


class Lightning:  # Air + Fire
    def __str__(self):
        return 'lightning'


class Dust:  # Air + Earth
    def __str__(self):
        return 'dust'


class Lava:  # Fire + Earth
    def __str__(self):
        return 'lava'


class Boy:
    def __add__(self, other):
        if isinstance(other, Girl):
            return Love()
        elif isinstance(other, Boy):
            return Pediki()
        else:
            return None


class Girl:
    def __add__(self, other):
        if isinstance(other, Girl):
            return LesbianLove()
        else:
            return None


class Love:  # Boy + Girl
    def __str__(self):
        return 'love <3'


class Pediki:
    def __str__(self):
        return 'pediki'


class LesbianLove:
    def __str__(self):
        return 'lesbian love'


first_component = Water()
second_component = Earth()
print(first_component + second_component)

