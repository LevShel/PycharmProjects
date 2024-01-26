input_text = input('Enter text: ').lower().split()
searching_words = input('Enter comma-separated searching words: ').lower().split(', ')

print('Counting words in text:')
for index in range(len(searching_words)):
    print(searching_words[index], ':', input_text.count(searching_words[index]))