from typing import List
from collections import deque

def solve(data: List[str]):

    data = [[x for x in row] for row in data] # convert to 2D array

    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    DEFAULT = 9
    M = len(data)
    N = len(data[0])
    neighbors = [[0 for _ in range(N)] for _ in range(M)]

    # the thing is, we don't need to loop through all M * N cells to determine which should be removed in this round
    # we can just loop through the cells that have neighbors < 4
    # then if we remove this, then update the neighbors. If the neighbor becomes < 4, then we add it to the list 
    # to be removed in the next round.

    # count neighbors
    queue = deque()
    seen = set()

    for i in range(M):
        for j in range(N):
            if data[i][j] != "@":
                neighbors[i][j] = DEFAULT
                continue
            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and data[ni][nj] == "@":
                    neighbors[i][j] += 1

            if neighbors[i][j] < 4:
                queue.append((i, j))
                seen.add((i, j))

    ans = 0
    while queue:
        # how many removed in this round
        i, j = queue.popleft()
        data[i][j] = "."
        ans += 1
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and neighbors[ni][nj] != DEFAULT:
                neighbors[ni][nj] -= 1
                if neighbors[ni][nj] < 4 and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    queue.append((ni, nj))

    print(ans)


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
