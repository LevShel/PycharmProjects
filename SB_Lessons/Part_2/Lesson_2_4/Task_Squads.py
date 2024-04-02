# Есть 2 отряда по 10 юнитов с рандомным уроном.
# Если сумма урона юнита 1 и 2 отряда больше 100, то юнит третьего отряда погибает.

import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3_condition = [('Died' if squad_1[i_damage] + squad_2[i_damage] > 100
                      else 'Survived')
                     for i_damage in range(10)]
print(squad_1)
print(squad_2)
print(squad_3_condition)