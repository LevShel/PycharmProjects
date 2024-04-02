# Если список:
scores = [54, 67, 48]

# Вариант 1 (через перебор)
# for i_player in range(len(scores)):
#     print(i_player, scores[i_player])

# Вариант 2 (мой)
# for i_player in scores:
#     print(scores.index(i_player)+1, i_player)

# Вариант 3 (через enumerate - из списка генерирем кортежи)
for i_player, i_score in enumerate(scores):
    print(i_player, i_score)


# Если словарь:
scores_dict = {
    'Vanya': 54,
    'Petya': 67,
    'Lena': 48
}

for i_name, i_score in scores_dict.items():
    print(i_name, i_score)