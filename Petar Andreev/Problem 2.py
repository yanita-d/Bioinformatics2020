input = open("data/sequence_1.seq", "r").read()
output = input[::-1]
print(output)
outFile = open("reverse_sequence_1.seq", "w")
outFile.write(output)
outFile.close()