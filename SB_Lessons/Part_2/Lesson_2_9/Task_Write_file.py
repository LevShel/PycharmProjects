speakers_file = open('speakers.txt', 'r', encoding='utf-8')
sym_count = [str(len(i_line)) for i_line in speakers_file]
sym_count_str = '\n'.join(sym_count)
speakers_file.close()

counts_file = open('sym_count.txt', 'w')
counts_file.write(sym_count_str)
counts_file.close()
