# Задача 1. Налоги
# Что нужно сделать
# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна
# состоять из базового класса Property и производных от него классов Apartment, Car
# и CountryHouse.
# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор,
# и метод расчёта налога, переопределённый в каждом из производных классов. Налог
# на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой
# параметр конструктору базового класса.
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество
# его денег и стоимость имущества, а затем выдаёт налог на соответствующее имущество
# и показывает, сколько денег ему не хватает (если это так).

class Property:
    def __init__(self, name, worth):
        self.name = name
        self.worth = float(worth)

    def tax_count(self):
        tax = 0
        if isinstance(self, Apartment):
            tax += self.worth / 1000
            return tax
        elif isinstance(self, Car):
            tax += self.worth / 200
            return tax
        elif isinstance(self, CountryHouse):
            tax += self.worth / 500
            return tax


class Apartment(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)


class Car(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)


class CountryHouse(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)


class User:
    def __init__(self, money=None):
        self.money = money if money else 0


user_1 = User()
user_1.money = float(input('Enter your budget: '))
total_tax = 0
while True:
    print('Enter info about your property:\n'
          '1. Apartment\n'
          '2. Car\n'
          '3. Country house\n'
          '4. EXIT')
    choice = int(input('>: '))
    if choice == 1:
        id_info = input('ID: ')
        price = float(input('Worth: '))
        my_apartment = Apartment(name=id_info, worth=price)
        total_tax += my_apartment.tax_count()
    elif choice == 2:
        model = input('ID: ')
        price = float(input('Worth: '))
        my_car = Car(name=model, worth=price)
        total_tax += my_car.tax_count()
    elif choice == 3:
        id_info = input('ID: ')
        price = float(input('Worth: '))
        my_country_house = CountryHouse(name=id_info, worth=price)
        total_tax += my_country_house.tax_count()
    elif choice == 4:
        break
print('Total tax is: ', total_tax)
if user_1.money > total_tax:
    print('You have enough money.')
else:
    print('You haven`t enough money for pay taxes.\n'
          f'More is needed: {total_tax-user_1.money}')