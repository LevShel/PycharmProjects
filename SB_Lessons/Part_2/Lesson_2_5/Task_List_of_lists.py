# Входные данные:
# Многомерный список
# [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
#
# Выходные данные:
# Одномерный список
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

start_list = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
output = [digit for each_list_1 in start_list for each_list_2 in each_list_1 for digit in each_list_2]

print('Start list: ', start_list)
print('Output list: ', output)