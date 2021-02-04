from Bio.Seq import Seq
from Bio import SeqIO

startCodon = 'AUG'
stopCodonsRNA = ['UAA', 'UAG', 'UGA']

def findLocations(s, t):
    result = []
    for idx in range(0, len(s) - len(t) + 1):
        if(s[idx : idx+len(t)] == t):
            result.append(idx)
    return result

def checkORF(orf):
    return any(list(map(lambda x: x % 3 == 0, [orf.find(stopCodonsRNA[0]), orf.find(stopCodonsRNA[1]), orf.find(stopCodonsRNA[2])])))

def readSeqFromFastaFile(filename):
    inputFileData = SeqIO.read(filename, "fasta")
    return inputFileData.seq

def getDistinctProteins(dnaSeq):
    rnaSequences = [dnaSeq.transcribe(), 
                    dnaSeq.transcribe()[1:], 
                    dnaSeq.transcribe()[2:], 
                    dnaSeq.reverse_complement().transcribe(), 
                    dnaSeq.reverse_complement().transcribe()[1:],
                    dnaSeq.reverse_complement().transcribe()[2:]]

    proteins = []

    for str in rnaSequences:
        for startIndex in findLocations(str, startCodon):
            orf = str[startIndex:]
            if checkORF(orf):
                proteins.append(orf.translate(to_stop = True).__str__())

    return list(set(proteins))

dnaSeq = readSeqFromFastaFile("data/fasta_seq_7.fa")
print(getDistinctProteins(dnaSeq))