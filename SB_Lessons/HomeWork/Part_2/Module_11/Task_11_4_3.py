# Задача 3. Весёлая ферма
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс
# «Грядка картошки».
# У картошки есть её номер в грядке, а также стадия зрелости. Она может
# предоставлять информацию о своей зрелости и расти. Всего у картошки может быть
# четыре стадии зрелости.
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может,
# собственно, взращивать всю эту картошку, а также предоставлять информацию о зрелости
# всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек
# и три раза взрастите грядку.
#
# Пример результата (проверка на зрелость и три взращивания):
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Росток
# Картошка 2 сейчас Росток
# Картошка 3 сейчас Росток
# Картошка 4 сейчас Росток
# Картошка 5 сейчас Росток
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зелёная
# Картошка 2 сейчас Зелёная
# Картошка 3 сейчас Зелёная
# Картошка 4 сейчас Зелёная
# Картошка 5 сейчас Зелёная
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зрелая
# Картошка 2 сейчас Зрелая
# Картошка 3 сейчас Зрелая
# Картошка 4 сейчас Зрелая
# Картошка 5 сейчас Зрелая
# Вся картошка созрела. Можно собирать!

class Potato:

    def __init__(self):
        self.state = 0

    def new_state(self):
        while self.state != 3:
            self.state += 1
            return self.state

    def print_info(self):
        if self.state == 0:
            print('There is nothing.\n')
        elif self.state == 1:
            print('Potato is sprout.\n')
        elif self.state == 2:
            print('Potato is green.\n')
        elif self.state == 3:
            print('Potato is ready.\n'
                  'And may be kept.\n')


# class Garden:

k = Potato()
k.print_info()
for i in range(3):
    k.new_state()
    k.print_info()