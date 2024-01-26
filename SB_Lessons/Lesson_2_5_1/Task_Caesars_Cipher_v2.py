def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 26] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = ('abcdefghij'    # 1...10
            'klmnopqrst'    # 11...20
            'uvwxyz')       # 21...26

in_string = input('Your message: ')
k = int(input('k = '))

caesar = caesar_cipher(in_string, k)
print("Caesar's cipher: ", caesar)