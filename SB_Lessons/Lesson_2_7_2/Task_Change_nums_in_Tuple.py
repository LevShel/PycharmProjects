def add_num(seq, number):
    seq = list(seq)
    for i_num in range(len(seq)):
        seq[i_num] += number
    return seq

origin_tuple = (1, 2, 3, 4, 5)
change_list = add_num(origin_tuple, 5)

print(origin_tuple)
print(change_list)