# Задача 3. Следим за расписанием
# Что нужно сделать
# После выполненной задачи Вася устал и понял, что весь следующий день
# ему придётся восстанавливать силы. Вася решил, что работать он будет
# только в чётные дни и написал небольшую программу, которая поможет ему
# не пропустить рабочий день.
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение.
# Подсказка: для проверки чётности используйте оператор %.

day = int(input('Enter day of month: '))

if day % 2 == 0:
    print('Day is even. Go to work!')
else:
    print('Day is odd. Have a nice rest!')