# words_list = []
# counts = [0, 0 ,0]
#
# num_words = int(input('Enter nums of searchig words: '))
#
# for i in range(num_words):
#     print('Enter ', i+1, ' searching word: ', end='')
#     word = input()
#     words_list.append(word)
#
# print('Enter text by words. Dot will end text.')
# text = input('>: ')
# while text != '.':
#     for i in range(num_words):
#         if words_list[i] == text:
#             counts[i] +=1
#     text = input('>: ')
#
# print('\n Counting words:')
# print('There are ', end='')
# for i in range(num_words):
#     print(counts[i], ' words "', words_list[i], '", ', end='')

words_list = [['',0],['',0],['',0]]

num_words = int(input('Enter nums of searchig words: '))

for i in range(num_words):
    print('Enter ', i+1, ' searching word: ', end='')
    word = input()
    words_list[i][0] = word

print('Enter text by words. Dot will end text.')
text = input('>: ')
while text != '.':
    for i in range(num_words):
        if words_list[i][0] == text:
            words_list[i][1] +=1
    text = input('>: ')

print('\n Counting words:')
print('There are ', end='')
for i in range(num_words):
    print(words_list[i][1], ' words "', words_list[i][0], '", ', end='')

input()