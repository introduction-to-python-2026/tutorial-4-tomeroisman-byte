def find_all_starts(dna):
    start = []
    for l in range(len(dna)-2):
        if dna[l: l+3] == "ATG":
            starts.append(i)
    return start

def find_first_in_register_stop(dna):
    stop_codon = []
    for i in range(len(dna)-2):
        if dna[i,i+3] in ("TAG", "TGA", "TAA"):
            stop_codon.append(i)
    return stop_codons


def all_orfs_range(dna):
    start = find_all_starts(dna)
    orf_ranges = []
    for s in start:
        end = find_first_in_register_stop(dna[s:])
        if end != -1:
            orf_ranges.append((s,s+end))
    return orf_ranges

def longest_orf(dna):
    longest = ""
    for orf_range in all_orfs_range(dna.upper()):
        orf = dna[orf_range[0]: orf_range[1]]
        if len(orf) > len(longest):
            longest = orf
    return longest



