def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return  sym_dict

text = input('Enter text: ').lower()
hist = histogram(text)

for i_sym in sorted(hist.keys()):
    print(i_sym, ' = ', hist[i_sym])

print('Maximum: ', max(hist.values()))