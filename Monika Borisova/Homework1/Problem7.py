from Bio import SeqIO
from Bio.Seq import Seq

f=open("orf.txt", "r")
sequence=f.read()

startCodon = "AUG"
codon_size = len(startCodon)
stopCodons = ["UAA","UAG","UGA"]
 
rna_seq = Seq(sequence).transcribe().__str__()
proteins=[]
rna_size = len(rna_seq)

for a in range(rna_size-codon_size):
    if rna_seq[a:a+codon_size]==startCodon:
        for stop in range(a,rna_size, 3):
            if stopCodons.__contains__(rna_seq[stop:stop+3]):
                proteins.append(Seq(rna_seq[a:stop]).translate())
                break


new_rna_seq = Seq(sequence).transcribe()
rna_reversed = new_rna_seq.reverse_complement()
reversed_size = len(rna_reversed)
for a in range(reversed_size-codon_size):
    if rna_reversed[a:a+codon_size]==startCodon:
        for stop in range(a, reversed_size, 3):
            if stopCodons.__contains__(rna_reversed[stop:stop+3]):
                proteins.append(rna_reversed[a:stop].translate())
                break

proteins = list(dict.fromkeys(proteins))
print(*proteins, sep = "\n")
