from typing import List, Optional, Tuple

def find_all_starts(dna: str) -> List[int]:
    dna = dna.upper()
    starts = []
    for pos in range(len(dna) - 2):
        if dna[pos:pos + 3] == "ATG":
            starts.append(pos)
    return starts

def find_first_in_register_stop(dna: str) -> Optional[int]:
    dna = dna.upper()
    for i in range(0, len(dna) - 2, 3):
        if dna[i:i+3] in ("TAA", "TAG", "TGA"):
            return i
    return None

def all_orfs_range(dna: str) -> List[Tuple[int, int]]:
    starts = find_all_starts(dna)
    orf_ranges = []
    for start in starts:
        end = find_first_in_register_stop(dna[start:])
        if end is not None:
            orf_ranges.append((start, start + end + 3))
    return orf_ranges

def longest_orf(dna: str) -> str:
    dna = dna.upper()
    longest = ""
    for start, stop in all_orfs_range(dna):
        orf = dna[start:stop]
        if len(orf) > len(longest):
            longest = orf
    return longest
