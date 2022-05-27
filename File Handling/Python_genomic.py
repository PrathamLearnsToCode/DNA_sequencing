# Computing the gc percentage
def gc(dna):
    nbases = dna.count("n") + dna.count("N")
    gc_percentage = float(dna.count("g") + dna.count("G") + dna.count("c") + dna.count("C"))*100.0/(len(dna) - nbases)
    return gc_percentage
print(gc("CGcgNnggggCCCgCgcgggcgCgnaaaTTT"))


# To check if a given DNA sequence contains an in-frame stop codons

dna = input("Enter the DNA sequence: ")


def has_stop_codon(dna):
    stop_codon_found = False
    stop_codons = ["tga", "tag", "taa"]
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


def reverse_string(seq):
    return seq[::-1]


def complement(seq):
    base_complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A',
                       'a': 't', 'g': 'c', 'c': 'g', 't': 'a'}
    letters = list(seq)
    letters = [base_complement[base] for base in letters]
    return ''.join(letters)


def reverse_complement(seq):
    seq = reverse_string(seq)
    seq = complement(seq)
    return seq


print(reverse_complement('CCGGCGATTTAG'))






