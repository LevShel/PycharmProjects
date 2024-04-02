def is_palindrome(string):
    char_dict = {}
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    print(char_dict)

    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    return odd_count <= 1

my_string = input('Enter string: ')
if is_palindrome(my_string):
    print('Palindrome possible')
else:
    print('Palindrome impossible')