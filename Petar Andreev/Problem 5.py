

dna = open("data\\dna_chromosome_1.seq", 'r')
d_sequence = dna.read()
dna.close()

r_sequence = d_sequence.replace('T', 'U')
r_reversed = r_sequence[::-1]

rna_file = open("reverse_rna.seq", "w")
rna_file.write(r_reversed)
rna_file.close()