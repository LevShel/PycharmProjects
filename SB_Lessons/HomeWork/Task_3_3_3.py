# Задача 3. Сложные степени
# Говорят, если в 22:31:49 посчитать на Python значение определённого выражения,
# то спустя год станешь очень хорошим программистом. Давайте проверим это утверждение.
#
# 1. Создайте переменную и запишите в неё следующее математическое выражение:
#
# 2. Затем выведите значение переменной на экран. Ответ должен быть равен 5916.36111111111.
# 3. Будьте внимательны со скобками, особенно с делением числителя на знаменатель.
#
# Подсказка
# Приоритет операций в python не отличается от приоритета, принятого в алгебре.
# Операции выполняются в следующем порядке
# Операции в скобках (a + b)
# Операции возведения в степень a**b
# Операции умножения и деления a * b
# Операции сложения и вычитания a + b - c
# Операции унарных плюсов и минусов -4
# Приоритеты всех операций вы сможете найти по ссылке Приоритет операций
# При равенстве приоритетов операции выполняются слева направо.
#
# При вычислении выражений с числителем и знаменателем, записанных в виде дробей
# будьте внимательны к тому, что весь числитель нужно разделить на весь знаменатель.
# Для этого можно отдельно вычислить числитель и отдельно знаменатель, а потом разделить
# числитель на знаменатель, либо поместить числитель и знаменатель в скобки.

result = (-3 + (((8 ** 2) - 12) * ((4 ** 3) ** 2)))/(2 * 18)
print(result)