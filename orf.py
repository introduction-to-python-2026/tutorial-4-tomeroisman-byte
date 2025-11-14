def find_all_starts(dna):
    dna = dna.upper()
    starts = []
    for i in range(len(dna) - 2):
        if dna[i:i+3] == "ATG":
            starts.append(i)
    return starts

def find_first_in_register_stop(dna, start):
    dna = dna.upper()
    i = start + 3
    while i <= len(dna) - 3:
        codon = dna[i:i+3]
        if codon == "TAA" or codon == "TAG" or codon == "TGA":
            return i
        i += 3
    return -1

def all_orfs_range(dna):
    dna = dna.upper()
    starts = find_all_starts(dna)
    orf_ranges = []
    for start in starts:
        stop = find_first_in_register_stop(dna, start)
        if stop != -1:
            orf_ranges.append((start, stop + 3))
    return orf_ranges

def longest_orf(dna):
    dna = dna.upper()
    orfs = all_orfs_range(dna)
    longest = ""
    for start, stop in orfs:
        orf = dna[start:stop]
        if len(orf) > len(longest):
            longest = orf
    if longest == "":
        return None
    return longest
