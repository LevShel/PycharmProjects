word = input('>: ')

print('First half: ', word[:(len(word)//2)])
first_half = word[:(len(word)//2)]
print('Second half: ', word[(len(word)//2):])
second_half = word[(len(word)//2):]
print('Reverse word by halfs: ', first_half[::-1]+second_half[::-1])