# Задача 3. Собачьи бега
# В собачьих бегах участвует N собак, у каждой из них есть определённое количество
# очков за сезон. На огромном табло выводятся очки каждой собаки. Однако при выводе
# был обнаружен баг: собаки с наибольшим и наименьшим количеством очков поменялись местами!
# Нужно это исправить.
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший
# и наименьший элементы в списке.

scores = [42, 23, 16, 15, 8, 4]
right_list = sorted(scores)
print(scores)
print(right_list)