# Задача 2. Автобус или метро?
# Для расчёта эффективности потраченных денег на метро и автобус Никита использует
# следующую формулу:
#
# В общем, не спрашивайте. Он написал программу для подсчёта формулы,
# но она почему-то не работает.
# bus = 5
# metro = 3
# result = (6 + 10 - bus * 2) / (bus + 1) + 132 / 2 + metro
# print(result)
# Скопируйте программу в редактор, исправьте выражение и убедитесь в правильности её работы.
# Правильный ответ: 26.607142857142858

bus = 5
metro = 3
result = ((6 + ((10 - bus) ** 2)) / (metro + 1)) + (132 / (2 + bus))
print(result)