alphabet = (' abcdefghij'   # 0, 1...10
            'klmnopqrst'    # 11...20
            'uvwxyz')       # 21...26

in_string = input('Your message: ')
caesar = []
k = int(input('k = '))

i = 0
j = 0
for _ in in_string:
    while in_string[i] != alphabet[j]:
        j += 1
    if k < len(alphabet):
        caesar.append(alphabet[k + j])
    if k > len(alphabet):
        caesar.append(alphabet[k + j - len(alphabet)])
    i += 1
    j = 0

print("Caesar's cipher: ", end='')
for symbol in caesar:
    print(symbol, end="")