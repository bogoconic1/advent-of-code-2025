from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solve(ranges: List[str], numbers: List[int]):

    # so you maintain a dict of numbers 
    # key N to key N+1 means that in this range, how many ranges contain each number from key N to (key N+1 - 1)
    # then we prefix sum over all the keys
    cached_range = defaultdict(int)
    ans = 0

    for r in ranges:
        start, end = r.split("-")
        start = int(start)
        end = int(end)
        cached_range[start] += 1
        cached_range[end+1] -= 1

    keys = sorted(cached_range.keys())
    for i in range(len(keys)-1):
        cached_range[keys[i+1]] += cached_range[keys[i]]

    for number in numbers:
        idxr = bisect_right(keys, number) - 1
        if idxr < 0:
            continue
        if cached_range[keys[idxr]] >= 1: ans += 1

    print(ans)



if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()

    # split by the '' element in the data list
    # ["3-5", "6-10", "", "2", "5"]
    line_break_index = data.index("")
    ranges = data[:line_break_index]
    numbers = [int(x) for x in data[line_break_index+1:]]

    solve(ranges, numbers)
