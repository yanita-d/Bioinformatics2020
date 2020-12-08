dna_file = open("data\\dna_chromosome_1.seq", 'r')
dna_seq = dna_file.read()
print(dna_seq)
dna_file.close()

rna_seq = dna_seq.replace('T', 'U')
revesed_seq = rna_seq[::-1]
print(revesed_seq)

rna_file = open("reversed_rna_seq.seq", "w")
rna_file.write(revesed_seq)
rna_file.close()