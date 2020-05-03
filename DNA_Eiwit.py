def dna_to_protein(seq):
    aa3 = {"A": ["GCU", "GCC", "GCA", "GCG"],
           "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
           "N": ["AAU", "AAC"],
           "D": ["GAU", "GAC"],
           "C": ["UGU", "UGC"],
           "Q": ["CAA", "CAG"],
           "E": ["GAA", "GAG"],
           "G": ["GGU", "GGC", "GGA", "GGG"],
           "H": ["CAU", "CAC"],
           "I": ["AUU", "AUC", "AUA"],
           "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
           "K": ["AAA", "AAG"],
           "M": ["AUG"],
           "F": ["UUU", "UUC"],
           "P": ["CCU", "CCC", "CCA", "CCG"],
           "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
           "T": ["ACU", "ACC", "ACA", "ACG"],
           "W": ["UGG"],
           "Y": ["UAU", "UAC"],
           "V": ["GUU", "GUC", "GUA", "GUG"],
           "*": ["UAG", "UGA", "UAA"]
            }
    stop = False
    j = 0
    eiwit = ""
    while not stop:
        codon = seq[3 * j:3 * (j + 1)]
        j += 1
        if codon == "":
            stop = True
        else:
            for i in aa3:
                if codon.upper().replace("T", "U") in aa3[i]:
                    eiwit += i
    return eiwit
