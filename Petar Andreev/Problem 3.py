
from Bio import SeqIO

seq_file = SeqIO.read("data//fasta_seq_1.fa", "fasta")
thymine_occurence = seq_file.seq.count("T") 
print("Thymine appears", str(thymine_occurence), "times in the sequence read.")