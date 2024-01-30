# Задача 4. Успеваемость в классе
# Что нужно сделать
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5,
# двоек сегодня не было. Напишите программу, которая получает
# список оценок — N чисел — и выводит на экран сообщение о том, кого сегодня больше:
# отличников, хорошистов или троечников.
# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

scores = []
pupils = int(input('Enter num of pupils: '))
threes = 0
fours = 0
fives = 0

for i in range(pupils):
    score = int(input(f'Enter score of {i+1} pupil: '))
    if score == 3:
        threes += 1
    elif score == 4:
        fours +=1
    else: fives += 1
    scores.append(score)
print('\nList of scores for today: ', end=' ')
for score in scores:
    print(score, end=' ')

max_scores = max(threes, fours, fives)
# if threes != fours != max_scores or threes != fives != max_scores or fours != fives != max_scores:
    # max_scores = max(threes, fours, fives)
if max_scores == threes and threes != fours and threes != fives:
    print('\n There were more threes today.')
elif max_scores == fours and fours != threes and fours != fives:
    print('\n There were more fours today.')
elif max_scores == fives and fives != threes and fives != fours:
    print('\n There were more fives today.')
elif max_scores == threes == fours != fives:
    print(('\n There were more threes and fours today.'))
elif max_scores == threes == fives != fours:
    print(('\n There were more threes and fives today.'))
elif max_scores == fours == fives != threes :
    print(('\n There were more fours and fives today.'))
else:
    print(('\n Today there were the same number of 3, 4 5.'))
