from typing import List
from bisect import bisect_left, bisect_right

INVALID_IDS = set([int(str(i) * 2) for i in range(100000)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 3) for i in range(10000)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 4) for i in range(1000)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 5) for i in range(100)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 6) for i in range(10)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 7) for i in range(10)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 8) for i in range(10)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 9) for i in range(10)]) # at most 10 digits
INVALID_IDS |= set([int(str(i) * 10) for i in range(10)]) # at most 10 digits
INVALID_IDS = list(INVALID_IDS)
INVALID_IDS.sort()

def solve(ids: List[str]):

    ids = [
        [int(x.split("-")[0]), int(x.split("-")[1])]
        for x in ids
    ]
    ans = 0
    for start, end in ids:
        idxl = bisect_left(INVALID_IDS, start)
        idxr = bisect_right(INVALID_IDS, end) - 1
        if idxl > idxr:
            continue
        ans += sum(INVALID_IDS[idxl:idxr+1])

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ids = open(os.path.join(dir_path, "input.txt"), "r").read().split(",")
    solve(ids)
