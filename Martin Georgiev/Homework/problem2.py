def reverseSeqFromFile(filename):
    inputFile = open(filename, "r")
    if inputFile.mode == 'r':
        seqData = inputFile.read()
        #revSeq = ''.join(reversed(seqData))
        reversedSeq = seqData[::-1]

    outputFile = open("reverse_sequence_1.seq", "w")
    outputFile.write(reversedSeq)
    outputFile.close()


#reverseSeqFromFile("data/sequence_1.seq")