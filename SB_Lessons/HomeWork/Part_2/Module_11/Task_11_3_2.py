# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома»
# и объекты которого могут выполнять следующие действия:
# 1.	Отобразить информацию о себе.
# 2.	Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# 3.	Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести
# соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
# Family name: Common family
# Family funds: 100000
# Having a house: False
#
# Try to buy a house
# Not enough money!
#
# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0
#
# Family name: Common family
# Family funds: 0.0
# Having a house: True

class Family:

    def __init__(self):
        self.name = 'Common family'
        self.funds = 100000
        self.house = False

    def try_to_buy_house(self, price):
        print('Try to buy house: ', end='')
        if self.funds >= price:
            print('House was bought!')
            self.funds -= price
            self.house = True
            return self.house, self.funds
        else:
            print('Not enough money...\n'
                  'Try later!')

    def earn_money(self, money):
        earned_money = money
        self.funds += earned_money
        print(f'Family earn {money}\n'
              f'Current funds: {self.funds}')
        return self.funds

    def print_info(self):
        print(f'Family name: {self.name}\n'
              f'Family funds: {self.funds}\n'
              f'Having a house: {self.house}')


print('=========')
family_1 = Family()
family_1.print_info()
print('=========')
family_1.earn_money(200000)
print('=========')
family_1.try_to_buy_house(500000)
print('=========')
family_1.earn_money(200000)
print('=========')
family_1.try_to_buy_house(500000)
print('=========')
family_1.print_info()
print('=========')