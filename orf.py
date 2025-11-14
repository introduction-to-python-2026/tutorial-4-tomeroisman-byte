def find_all_starts(dna):
    starts = []
    for _1 in range(len(dna)-2):
        if dna[_1: _1+3] == "ATG":
            starts.append(_1)
    return starts

def find_first_in_register_stop(dna):
    for _2 in range(0, len(dna) - 2, 3):
        if dna[_2:_2+3] in ("TAA", "TAG", "TGA"):
            return _2
    return None

def all_orfs_range(dna):
    starts = find_all_starts(dna)
    orf_ranges = []
    for start in starts:
        end = find_first_in_register_stop(dna[start:])
        if end is not None:
            orf_ranges.append((start,start + end))
    return orf_ranges

def longest_orf(dna):
    dna = dna.upper()
    longest = ""
    for start, stop in all_orfs_range(dna):
        orf = dna[start:stop]   
        if len(orf) > len(longest):
            longest = orf
    return longest


