from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# task 1
def find_adenine_count(seq):
    print("Adenine frequency:", seq.count("A"))

# task 2
def reverse_seq():
    with open("data/sequence_1.seq", "r") as seq, \
         open("reverse_sequence_1.seq", "w") as reverse_seq:
        reverse_seq.write(seq.readline()[::-1])

# task 3
def find_thymine_count():
    with open("data/fasta_seq_1.fa", "r") as fasta_seq:
        for record in SeqIO.parse(fasta_seq, "fasta"):
            print("Thymine frequency:", record.seq.count("T"))

# task 4
def chromosome_solve():
    with open("data/dna_chromosome_1.seq", "r") as input_file, \
         open("dna_chromosome_solve_1.seq", "w") as dna_solve:
        for dna in input_file:
            for base in dna:
                if base == "A":
                    dna_solve.write("T")
                elif base == "T":
                    dna_solve.write("A")
                else:
                    dna_solve.write(base)

# task 5
def reverse_transcription():
    with open("data/dna_chromosome_1.seq", "r") as input_file, \
         open("rna_reverse_1.seq", "w") as output_file:
        rna = ""
        for dna in input_file:
            for base in dna:
                if base == "T":
                    rna += "U"
                else:
                    rna += base
        output_file.write(rna[::-1])

# task 6
def find_substrings(string, substring):
    indices = []
    for i in range(len(string)):
        if string[i:].startswith(substring):
            indices.append(i + 1)
    return indices

# task 7
def rna_to_protein(rna):
    start_codons = ["AUG"]
    stop_codons = ["UAG", "UAA", "UGA"]

    start_codon_indices = find_substrings(rna, start_codons[0])
    stop_codon_indices = find_substrings(rna, stop_codons[0]) + \
                         find_substrings(rna, stop_codons[1]) + \
                         find_substrings(rna, stop_codons[2])
    stop_codon_indices.sort()

    proteins = []
    for start_codon in start_codon_indices:
        for stop_codon in stop_codon_indices:
            if start_codon < stop_codon and (stop_codon - start_codon) % 3 == 0:
                proteins.append(str(rna[start_codon - 1:stop_codon - 1].translate()))
                break
    return proteins


def dna_to_protein():
    with open("data/open_reading_frames.fasta", "r") as input_file:
        for record in SeqIO.parse(input_file, "fasta"):
            rna = record.seq.transcribe()
            proteins = rna_to_protein(rna) + rna_to_protein(rna.reverse_complement())
            print("\n".join(set(proteins)))
            

find_adenine_count("ATAGTGGGAAGATTTATA")
reverse_seq()
find_thymine_count()
chromosome_solve()
reverse_transcription()
print(*(find_substrings("GATATATGCATATACTT", "ATAT")))
dna_to_protein()
