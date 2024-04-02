class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'yes' if self.has_tail else 'no'
        return (f'Legs: {self.legs},\n'
                f'has tail: {tail}\n')


class Cat(Pet):
    def sound(self):
        return 'Myau\n'


class Dog(Pet):
    def sound(self):
        return 'Gav\n'


class Frog(Pet):
    has_tail = False

    def sound(self):
        return 'Qua\n'


cat = Cat()
dog = Dog()
frog = Frog()
print(cat,
      cat.sound(),
      dog,
      dog.sound(),
      frog,
      frog.sound())
