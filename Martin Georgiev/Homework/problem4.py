changeNucleotide = {'A': 'T', 'T': 'A'}

def manipulateSeqFromFile(filename):
    inputFile = open(filename, "r")
    if inputFile.mode == 'r':
        seqData = inputFile.read()
        changedDNASeq = changeDNASeq(seqData)
    
    outputFile = open("dna_chromosome_solve_1.seq", "w")
    outputFile.write(changedDNASeq)
    outputFile.close()

def changeDNASeq(seqData):
    changedDNA = ''
    for idx in range(0, len(seqData)):
        if(seqData[idx] == 'A' or seqData[idx] == 'T'):
            changedDNA += changeNucleotide[seqData[idx]]
        else:
            changedDNA += seqData[idx]
    return changedDNA

#manipulateSeqFromFile("data/dna_chromosome_1.seq")