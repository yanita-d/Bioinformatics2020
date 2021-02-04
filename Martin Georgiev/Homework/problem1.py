from Bio.Seq import *
from collections import Counter

dnaSeq = Seq("ATAGTGGGAAGATTTATA");

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