#problem 1

from Bio.Seq import Seq

print(Seq("ATAGTGGGAAGATTTATA").count("A"))

#problem 2
mySeq = open("data/sequence_1.seq", "r").read()
revSeq = mySeq[::-1]

outFile = open("reverse_sequence_1.seq", "w")
outFile.write(revSeq)
outFile.close()

#problem 3
from Bio import SeqIO

print(SeqIO.read("data/fasta_seq_1.fa", "fasta").seq.count("T"))

#problem 4
mySeq = open("data/dna_chromosome_1.seq", "r").read()

outFile = open("dna_chromosome_solve_1.seq", "w")
for nuc in mySeq:
    if nuc == 'A':
        outFile.write('T')
    elif nuc == 'T':
        outFile.write('A')
    else:
        outFile.write(nuc)
outFile.close()

#problem 5
mySeq = open("data/dna_chromosome_1.seq", "r").read().strip()

outFile = open("reverse_rna_sequence_1.seq", "w")
outFile.write(Seq(mySeq[::-1]).transcribe().__str__())
outFile.close()

#problem 6
def startIndices(str, substr):
    startInd = []
    startIndex = str.find(substr)
    while(startIndex != -1):
        startInd.append(startIndex)
        startIndex = str.find(substr, startIndex+1)
    return startInd

s = "GATATATGCATATACTT"
t = "ATAT"

print(list(map(lambda x: x+1, startIndices(s, t))))

#problem 7
def expressibleGenes(dna):
    startCodon = "AUG"
    RNATranscripts = [Seq(dna).transcribe(), Seq(dna).transcribe().reverse_complement()]
    genes = []
    for RNATranscript in RNATranscripts:
        for startCodonIndex in startIndices(RNATranscript, startCodon):
            newGene = RNATranscript[startCodonIndex:].translate()
            if "*" in newGene:
                genes.append(newGene.split("*")[0].__str__())
    return list(set(genes))

print(expressibleGenes("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"))