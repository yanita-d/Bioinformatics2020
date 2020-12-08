old_file = open("data\\dna_chromosome_1.seq", "r")
old_seq = old_file.read()
print(old_seq)
old_file.close()

old_seq = old_seq.replace('A', 'W')
old_seq = old_seq.replace('T', 'A')
old_seq = old_seq.replace('W', 'T')
new_seq = old_seq
print(new_seq)

new_file = open("dna_chromosome_solve_1.seq", "w")
new_file.write(new_seq)
new_file.close()
