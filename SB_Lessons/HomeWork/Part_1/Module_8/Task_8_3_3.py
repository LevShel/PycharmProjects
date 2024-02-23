# Задача 3. Диета
# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать.
# Питается Саша следующим образом: каж-дые 3 часа он выпивает литр воды и съедает N калорий.
# Пить и есть он, кстати, начинает сразу как только проснётся. Напишите программу,
# которая считает сколько он выпьет литров воды и сколько калорий он съест
# перед тем как пойдёт спать.

# Исходные данные
water = 0
total_calories = 0
max_calories = 2000
wake_up = 0
sleep_time = 2300

# Проснулся
wake_up = int(input('What time is it? '))
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