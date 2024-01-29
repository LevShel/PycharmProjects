# Задача 3. Поел — можно и поспать, поспал — можно и поесть
# Напишите программу, разобранную в уроке.
# У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью,
# но засыпает всегда до того, как наступит полночь, обычно в 23 часа. А ещё он очень любит поесть.
# Он ест каждый час и если съедает больше 2000 калорий, то он просто падает спать.
# Напишите программу, которая поможет Саше понять, всё ли с ним хорошо.
# Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.

# Исходные данные
water = 0
total_calories = 0
max_calories = 2000
wake_up = None
sleep_time = 2300

# Проснулся
wake_up = int(input('What time is it? (hhmm) '))
print()

# Цикл от проснулся до пора спать
for hour in range(wake_up, sleep_time + 100, 100):

    # Если не набрал калорий
    if total_calories < max_calories:
        print('Now is:', hour, "o'clock")
        calories = int(input('How much calories you eat? '))
        total_calories += calories
        water += 1
        print()
        print('You drink ', water, ' liter of water and eat', total_calories / 1000, 'kcal')
        print()
        print('=========')
        print()

    # Если набрал больше 2к калорий
    elif total_calories >= max_calories:
        print('You drink ', water, ' liter of water and eat', total_calories / 1000, 'kcal')
        print('Go to sleep at ', hour - 100, '!')
        break

    # Если 23:00, то пора спать
    if hour == sleep_time:
        print('Now is ', sleep_time, "o'clock. You drink ", water, ' liter of water and eat', total_calories / 1000,
              'kcal. Go to sleep!')