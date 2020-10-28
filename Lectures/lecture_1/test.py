from Bio.Seq import Seq
from collections import Counter
from collections import defaultdict
from Bio import SeqIO
from Bio.SeqUtils import GC

for seq_record in SeqIO.parse("fastam.txt", "fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    print("gc = " + str(GC(seq_record.seq)))

seqFile = open("fastam.txt", "r")
fastaList = []
currentSeq = ""

for line in seqFile:
    if line[0] == ">":
        if currentSeq != "":
            fastaList.append(currentSeq)
        currentSeq = [line.lstrip(">").rstrip("\n"), ""]  

elements = Counter("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print((elements["G"] + elements["C"])/(elements["G"] + elements["C"] + elements["T"] + elements["A"]))

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq.transcribe())
