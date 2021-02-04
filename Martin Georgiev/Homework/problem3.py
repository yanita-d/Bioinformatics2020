from Bio import SeqIO
from collections import Counter

#reading fasta format file and returning the sequence
def readSeqFromFastaFile(filename):
    inputFileData = SeqIO.read(filename, "fasta")
    return inputFileData.seq

dnaSeq = readSeqFromFastaFile("data/fasta_seq_1.fa")

#first way
def myFrequencyTable(dnaSeq):
    frequencyTable = {'A': 0, 'C': 0,'G': 0,'T': 0}
    for nuc in dnaSeq:
        frequencyTable[nuc] += 1
    print(frequencyTable['A'])

#second way
def collectionsFrequencyTable(dnaSeq):
    frequencyTable2 = Counter(dnaSeq)
    print(frequencyTable2['A'])

#third way
def bioModuleFrequency(dnaSeq):
    print(dnaSeq.count('A'))

myFrequencyTable(dnaSeq)
collectionsFrequencyTable(dnaSeq)
bioModuleFrequency(dnaSeq)