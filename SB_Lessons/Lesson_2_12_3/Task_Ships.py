class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'Model of ship: {self.__model}.'

    def sail(self):
        return 'Ship is going now.'


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        return f'Ship attacks by {self.gun}'


class CargoShip(Ship):
    # TODO
    pass


warship = WarShip('qwerty', 'torpeda')
print(warship, warship.attack())