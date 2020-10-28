from Bio.Seq import Seq
from collections import Counter
from collections import defaultdict
from Bio import SeqIO
from Bio.SeqUtils import GC

dna_groups = []
for seqElement in SeqIO.parse("sequences.fasta", "fasta"):
    dna = seqElement.seq
    in_group = False
    for index, group in enumerate(dna_groups):
        if dna in group:
            in_group = True
            dna_groups[index].append(dna)
            break
        if dna.reverse_complement() in group:
            in_group = True
            dna_groups[index].append(dna)
            break
    
    if not in_group:
        dna_groups.append([dna])

seq_errors = []
seq_correct = []
seq_separated = [[],[]]

while len(dna_groups) > 0:
    lastIndex = len(dna_groups) - 1
    lastGroup = dna_groups[lastIndex]
    groupLen = len(lastGroup)
    lastElement = dna_groups.pop(lastIndex)
    if groupLen > 1:
        seq_correct.append(lastElement)
    else:
        seq_errors.append(lastElement)

print(len(seq_errors))
print(len(seq_correct))