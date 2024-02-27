# Задача 3. Лавка
# В небольшой фруктовой лавке у каждого фрукта есть название и цена. Эта информация
# хранится в одном большом списке, вот так:
# goods = [["яблоки", 50], ["апельсины", 190],
#           ["груши", 100], ["нектарины", 200], ["бананы", 77]]
# Недавно в лавку привезли новый fruit_name по цене price, а после этого случилось
# ужасное: повысили налоги. А значит, повысились и цены на фрукты, на целых 8%!
# Реализуйте код, который добавляет в список goods ещё один список с новым фруктом
# и ценой (это запрашивается у пользователя), а затем увеличивает цены всех фруктов на 8%.
#
# Пример:
# Текущий ассортимент: [["яблоки", 50], ["апельсины", 190],
#                       ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# Новый фрукт: абрикосы
# Цена: 150
#
# Новый ассортимент: [["яблоки", 50], ["апельсины", 190], ["груши", 100],
#                       ["нектарины", 200], ["бананы", 77], ["абрикосы", 150]]
#
# Новый ассортимент с увел. ценой: [['яблоки', 54.0], ['апельсины', 205.2], ['груши', 108.0],
#                            ['нектарины', 216.0], ['бананы', 83.16], ['абрикосы', 162.0]]

goods = [["яблоки", 50],
         ["апельсины", 190],
         ["груши", 100],
         ["нектарины", 200],
         ["бананы", 77]]

fruit_name = input('New fruit: ')
price = int(input(f'Price of {fruit_name}: '))
new_fruit = [fruit_name, price]
goods.append(new_fruit)
print(f'\nNew assortment: {goods}\n')
for fruit in goods:
    old_price = fruit[1]
    new_price = old_price + old_price*0.08
    fruit.remove(old_price)
    fruit.insert(1, new_price)
print(f'New assortment after prices up: {goods}')