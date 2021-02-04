
def adenine_frequency(sequence, nucleotide):
    counter = 0
    for s in sequence:
        if s == nucleotide:
            counter +=1
    
    return counter


sequence = "ATAGTGGGAAGATTTATA"
adenine_count = adenine_frequency(sequence, 'A')    
print(adenine_count)