from typing import List, Tuple, Optional
def find_all_starts(dna: str) -> List[int]:
    dna = dna.upper()
    starts = []
    for pos in range(len(dna) - 2):
        if dna[pos:pos + 3] == "ATG":
            starts.append(pos)
    return starts
def find_first_in_register_stop(dna: str) -> int:
    dna = dna.upper()
    for i in range(0, len(dna) - 2, 3):
        if dna[i:i + 3] in ("TAA", "TAG", "TGA"):
            return i
    return -1
def all_orfs_range(dna: str) -> List[Tuple[int, int]]:
    dna = dna.upper()
    starts = find_all_starts(dna)
    orf_ranges = []
    for start in starts:
        stop_index = find_first_in_register_stop(dna[start:])
        if stop_index != -1:
            orf_ranges.append((start, start + stop_index))
    return orf_ranges
def longest_orf(dna: str) -> Optional[str]:
    dna = dna.upper()
    orfs = all_orfs_range(dna)
    if not orfs:
        return None
    longest = ""
    for start, stop in orfs:
        orf = dna[start:stop]
        if len(orf) > len(longest):
            longest = orf
    return longest
