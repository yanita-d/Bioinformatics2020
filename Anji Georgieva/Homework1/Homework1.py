from Bio.Seq import Seq
from Bio import SeqIO

# Zad 1
my_seq=Seq("ATAGTGGGAAGATTTATA")
print (my_seq.count("A"))

# Zad 2
seqFile=open("data\\sequence_1.seq", "r")
seq=seqFile.read()
rev=seq[::-1]
print(rev)
reverseSeq=open("reverse_sequence_1.seq", "w")
reverseSeq.write(rev)
reverseSeq.close()

# Zad 3
record = SeqIO.read("data\\fasta_seq_1.fa", "fasta")
print(record.seq.count("T"))

# Zad 4
dnaFile=open("data\\dna_chromosome_1.seq", "r")
my_seq=dnaFile.read()

dnaSeq=open("dna_chromosome_solve_1.seq", "w")
for dna in my_seq: 
    if dna=="A":
        dnaSeq.write("T")
    elif dna=="T":
        dnaSeq.write("A")
    else :
        dnaSeq.write(dna)
dnaSeq.close()

# Zad 5
dnaSeq=open("data\\dna_chromosome_1.seq", "r")
my_seq=dnaSeq.read()
print(my_seq)
RNA=Seq(my_seq).transcribe()

rev=RNA[::-1]
print(rev)
reverseRNASeq=open("reverse_RNAsequence_1.seq", "w")
reverseRNASeq.write(rev.__str__())
reverseRNASeq.close()

# Zad 6
mySeq=open("sampleData.txt", "r")
my_seq=mySeq.read()
#print(my_seq)
s, t=my_seq.split("\n")
print("s: " + s)
print("t: " + t)

for n in range(len(s)-len(t)):
    if t==s[n:(len(t)+n)]:
        print(n+1)
    

# Zad 7
mySeq=open("seqSampleData.txt", "r")
my_seq=mySeq.read()

# RNA transcribe
RNA=Seq(my_seq).transcribe().__str__()


startCodon="AUG"
stopCodons=["UAA","UAG","UGA"]

# RNA to amino acid
for st in range(len(RNA)-len(startCodon)):
    if RNA[st:st+len(startCodon)]==startCodon:
      
        for stop in range(st,len(RNA),3):
            if stopCodons.__contains__(RNA[stop:stop+3]):
                print(Seq(RNA[st:stop]).translate())
                break

# Reverse complement RNA to amino acid
compRNA=Seq(RNA).complement()
revRNA=compRNA[::-1]
for st in range(len(revRNA)-len(startCodon)):
    if revRNA[st:st+len(startCodon)]==startCodon:
      
        for stop in range(st,len(revRNA),3):
            if stopCodons.__contains__(revRNA[stop:stop+3]):
                print(revRNA[st:stop].translate())
                break
