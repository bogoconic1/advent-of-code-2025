"""
  Y
   8 │ ............
   7 │ ........●─●.     ← (9,7) and (11,7)
   6 │ ........│.│.
   5 │ .●──────●.│.     ← (2,5) and (9,5)
   4 │ .│........│.
   3 │ .●────●...│.     ← (2,3) and (7,3)
   2 │ ......│...│.
   1 │ ......●───●.     ← (7,1) and (11,1)
   0 │ ............
     └─────────────
        2 4 6 8 10 12 X         
"""

from typing import List
from collections import defaultdict
from bisect import bisect_left

def solve(data: List[str]):

    data = [[int(y) for y in x.split(",")] for x in data]
    all_x = sorted(list(set([x for x, y in data])))
    ans = 0

    '''
    for each x find the min and max y
    they will never overlap
    '''
    xd = defaultdict(list)
    yd = defaultdict(list)
    for x, y in data:
        xd[x].append(y)
        yd[y].append(x)

    ylow, yhigh = [], []
    start_low, start_high = [(min(xd), min(xd[min(xd)])), (min(xd), max(xd[min(xd)]))]
    end_low, end_high = [(max(xd), min(xd[max(xd)])), (max(xd), max(xd[max(xd)]))]
    ylow.append(start_low)
    yhigh.append(start_high)

    # trace the path from start_low to end_low
    direction = "X"
    while start_low != end_low:
        if direction == "X":
            # search yd, go horizontal
            for x in yd[start_low[1]]:
                if x != start_low[0]:
                    start_low = (x, start_low[1])
                    ylow.append(start_low)
                    break
        else:
            # search xd, go vertical
            for y in xd[start_low[0]]:
                if y != start_low[1]:
                    start_low = (start_low[0], y)
                    ylow.append(start_low)
                    break
        
        direction = "Y" if direction == "X" else "X"

    
    # trace the path from start_high to end_high
    direction = "X"
    while start_high != end_high:
        if direction == "X":
            # search yd, go horizontal
            for x in yd[start_high[1]]:
                if x != start_high[0]:
                    start_high = (x, start_high[1])
                    yhigh.append(start_high)
                    break
        else:
            # search xd, go vertical
            for y in xd[start_high[0]]:
                if y != start_high[1]:
                    start_high = (start_high[0], y)
                    yhigh.append(start_high)
                    break
        direction = "Y" if direction == "X" else "X"

    minimums, maximums = {}, {}
    # then slide the window over all_x
    # minimum first
    ptr = 0
    for x in all_x:
        while ptr < len(ylow) and ylow[ptr][0] < x:
            ptr += 1
        minimums[x] = ylow[ptr][1]
        while ptr < len(ylow) and ylow[ptr][0] == x:
            minimums[x] = min(minimums[x], ylow[ptr][1])
            ptr += 1

    # maximum next
    ptr = 0
    for x in all_x:
        while ptr < len(yhigh) and yhigh[ptr][0] < x:
            ptr += 1
        maximums[x] = yhigh[ptr][1]
        while ptr < len(yhigh) and yhigh[ptr][0] == x:
            maximums[x] = max(maximums[x], yhigh[ptr][1])
            ptr += 1

    # for each pair check if valid
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            pt1 = data[i]
            pt2 = data[j]

            if not (minimums[pt1[0]] <= pt2[1] <= maximums[pt1[0]] and minimums[pt2[0]] <= pt1[1] <= maximums[pt2[0]]):
                continue

            ans = max(ans, (abs(pt1[0] - pt2[0]) + 1) * (abs(pt1[1] - pt2[1]) + 1))

    print(ans)



if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
