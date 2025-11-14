def find_all_starts(dna):
    starts = []
    for l in range(len(dna)-2):
        if dna[l: l+3] == "ATG":
            starts.append(l)
    return starts

def find_first_in_register_stop(dna):
    for i in range(0, len(dna) - 2, 3):
        if dna[i:i+3] in ("TAA", "TAG", "TGA"):
            return i
    return None

def all_orfs_range(dna):
    starts = find_all_starts(dna)
    orf_ranges = []
    for s in starts:
        end = find_first_in_register_stop(dna[s:])
        if end is not None:
            orf_ranges.append((s,s+end))
    return orf_ranges

def longest_orf(dna):
    dna = dna.upper()
    longest = ""
    for start, stop in all_orfs_range(dna.upper()):
        orf = dna[start:stop]   
        if len(orf) > len(longest):
            longest = orf
    return longest


