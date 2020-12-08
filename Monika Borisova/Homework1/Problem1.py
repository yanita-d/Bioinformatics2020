from collections import defaultdict

def nucleotide_count(sequence, nucleotide):
    counter = 0
    for n in sequence:
        if n == nucleotide:
            counter +=1
    
    return counter


def main():
    sequence = "ATAGTGGGAAGATTTATA"
    adenine_count = nucleotide_count(sequence, 'A')
    print("The frequency of adenine occurence is: " + str(adenine_count))
            
if __name__ == "__main__":
    main()