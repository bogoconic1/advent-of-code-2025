from typing import List

def solve(data: List[str]):

    data = [[x for x in row] for row in data] # convert to 2D array

    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    M = len(data)
    N = len(data[0])
    ans = 0
    while True:
        # how many removed in this round
        local_ans = 0
        for i in range(M):
            for j in range(N):
                if data[i][j] != "@":
                    continue

                adj_count = 0
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N:
                        if data[ni][nj] == "@":
                            adj_count += 1

                if adj_count < 4:
                    data[i][j] = "."
                    local_ans += 1

        if local_ans == 0:
            break
        ans += local_ans

    print(ans)


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
