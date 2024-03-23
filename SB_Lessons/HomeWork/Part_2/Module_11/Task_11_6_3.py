# Задача 3. Отцы, матери и дети
# Что нужно сделать
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# •	имя,
# •	возраст,
# •	список детей.
# И он может:
# •	сообщить информацию о себе,
# •	успокоить ребёнка,
# •	покормить ребёнка.
# У ребёнка есть:
# •	имя,
# •	возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# •	состояние спокойствия,
# •	состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_info(self):
        print(f'\tParent:\n'
              f'{self.name}, {self.age} y.o.\n'
              f'have {len(self.children)} children: ', end='')
        print(', '.join(child.name for child in self.children), '\n')

    def calm_child(self, child):
        child.calm()

    def feed_child(self, child):
        child.feed()


class Child:
    def __init__(self, name, age, parent):
        self.name = name
        self.age = age
        self.parent = parent
        if (self.parent.age - self.age) < 16:
            print(f'\n\tWrong age! {self.name} is very old!\n')
        self.calmness = False  # True - calm, False - upset
        self.hunger = True  # True - hungry, False - not hungry

    def calm(self):
        self.calmness = True

    def upset(self):
        self.calmness = False

    def feed(self):
        self.hunger = False

    def print_info(self):
        print(f'\tChild of {self.parent.name}:\n'
              f'{self.name}, {self.age} y.o.\n'
              f'Calm: {self.calmness}\n'
              f'Hunger: {self.hunger}\n')


father = Parent('Papa', 40)
daughter = Child('Do4ka', 10, father)
son = Child('Syn', 5, father)
father.add_child(daughter)
father.add_child(son)

father.print_info()
for child in father.children:
    child.print_info()

print('!!! Need to calm and feed.')
father.calm_child(daughter)
father.calm_child(son)
father.feed_child(daughter)
father.feed_child(son)
for child in father.children:
    child.print_info()