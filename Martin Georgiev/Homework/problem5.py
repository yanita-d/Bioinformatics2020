from Bio.Seq import *

def manipulateSeqFromFile(filename):
    inputFile = open(filename, "r")
    if inputFile.mode == 'r':
        seqData = inputFile.read()
        rnaSeq = transcription(seqData)
    
    outputFile = open("rna_sequence_solve_1.seq", "w")
    outputFile.write(rnaSeq.__str__())
    outputFile.close()
    
def transcription(seqData):
    dnaSeq = Seq(seqData[::-1])
    return dnaSeq.transcribe()

#manipulateSeqFromFile("data/dna_chromosome_1.seq")