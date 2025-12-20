from typing import List

def solve(data: List[str]):

    data = [[int(y) for y in x.split(",")] for x in data]

    ans = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ans = max(ans, (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1))

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
