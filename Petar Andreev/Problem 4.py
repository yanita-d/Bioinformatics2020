

initialChromosome=open("data\\dna_chromosome_1.seq", "r")
chromosome = initialChromosome.read()

seq=open("dna_chromosome_solve_1.seq", "w")
for sequention in chromosome: 
    if sequention =="A":
        seq.write("T")
    elif sequention =="T":
        seq.write("A")
    else :
        seq.write(sequention)
seq.close()