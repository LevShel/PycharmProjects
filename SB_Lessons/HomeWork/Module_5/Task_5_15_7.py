# Задача 7. Почта
# Что нужно сделать
# Почтовое отделение открывается в 08:00 и закрывается в 22:00. С 14:00 до 15:00
# все сотрудники уходят на обед, а в 10:00 и 18:00 приезжают машины с посылками,
# и все сотрудники на два часа заняты их разгрузкой. Во время обеда и разгрузки машин
# посылки никто не выдаёт.
# Напишите программу, которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку. Используйте только один условный оператор if-else,
# без elif и прочих. Решите задание двумя способами:
# 1.	При выполнении условия выводится сообщение: «Можно получить посылку».
# 2.	При выполнении условия выводится сообщение: «Посылку получить нельзя».
# Советы и рекомендации
# Обратите внимание на количество условий и постарайтесь сократить их.
# Не используйте перечисление конкретных часов вида a == 1 and a == 2...

open_time = 8
close_time = 22
dinner_start = 14
dinner_finish = 15
first_unload_start = 10
first_unload_finish = 12
second_unload_start = 18
second_unload_finish = 20

visit = int(input('What time is it? '))

if (open_time <= visit < first_unload_start) or (first_unload_finish <= visit < dinner_start) or (dinner_finish <= visit < second_unload_start) or (second_unload_finish <= visit < close_time):
    print('Welcome!')
elif close_time <= visit or visit < open_time:
    print('Post office is closed!')
else:
    print('All personal are busy!')