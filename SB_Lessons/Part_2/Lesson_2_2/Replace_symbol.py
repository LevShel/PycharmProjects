Word = input('Enter word: ')
NumReplaceSymbol = int(input('Number of replaced symbol: '))
NewSymbol = input('Enter new symbol: ')

            # ВАРИАНТ 1
#
# NewWord = ''
#
# Count = 0
#
# for Symbol in Word:
#     Count += 1
#     if Count != NumReplaceSymbol:
#         NewWord += Symbol
#     else:
#         NewWord += NewSymbol
#
# print('New word is: ', NewWord)

            # ВАРИАНТ 2
#
# SymList = []
#
# for Sym in Word:
#     SymList.append(Sym)
# SymList[NumReplaceSymbol-1] = NewSymbol

            # ВАРИАНТ 3
SymList = list(Word)
SymList[NumReplaceSymbol-1] = NewSymbol

for i in SymList:
    print(i, end='')