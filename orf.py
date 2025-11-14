def find_all_starts(dna):
    dna = dna.upper()
    starts = []
    for i in range(len(dna) - 2):
        if dna[i:i+3] == "ATG":
            starts.append(i)
    return starts

def find_first_in_register_stop(dna, start):
    dna = dna.upper()
    for i in range(start, len(dna) - 2, 3):
        if dna[i:i+3] in ("TAA", "TAG", "TGA"):
            return i
    return -1

def all_orfs_range(dna):
    dna = dna.upper()
    orf_ranges = []
    # Check each of the three reading frames
    for frame in range(3):
        i = frame
        while i <= len(dna) - 3:
            codon = dna[i:i+3]
            if codon == "ATG":
                stop = find_first_in_register_stop(dna, i + 3)
                if stop != -1:
                    orf_ranges.append((i, stop + 3))
                    i = stop + 3
                    continue
            i += 3
    return orf_ranges

def longest_orf(dna):
    dna = dna.upper()
    orfs = all_orfs_range(dna)
    if not orfs:
        return None
    longest_seq = ""
    for start, stop in orfs:
        seq = dna[start:stop]
        if len(seq) > len(longest_seq):
            longest_seq = seq
    return longest_seq
