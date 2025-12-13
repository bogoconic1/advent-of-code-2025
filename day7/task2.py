from typing import List
from pprint import pprint

'''
Row             dp
.......S....... [0]
............... [0]
.......^....... [2]
............... [2]
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
'''

def solve(data: List[str]):

    M = len(data)
    N = len(data[0])

    dp = [[0 for _ in range(N)] for _ in range(M)]
    dp[0][data[0].index("S")] = 1

    # the last row is all dots (so no edge case)\
    # the edge case # ^^ cannot happen
    # also edge case ^ at leftmost and rightmost cannot happen, so j-1 and j+1 is safe
    for i in range(M-1):
        for j in range(N):
            if data[i+1][j] == "^":
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j+1] += dp[i][j]
            else:
                dp[i+1][j] += dp[i][j]

    print(sum(dp[M-1]))

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
