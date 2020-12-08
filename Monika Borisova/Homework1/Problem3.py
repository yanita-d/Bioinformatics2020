from Bio import SeqIO
from Bio import Seq

fasta_seq = SeqIO.read("data//fasta_seq_1.fa", "fasta")
thymine_counter = fasta_seq.seq.count("T") 
print("The frequency of thymine occurence is: " + str(thymine_counter))
