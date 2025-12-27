from typing import List, Tuple

def parse(data: List[str]) -> Tuple[List[List[str]], List[Tuple[List[int], List[int]]]]:
    grids = []
    queries = []

    i = 0
    while i < len(data) and len(grids) < 6:
        line = data[i]
        if line and line[0].isdigit() and line.endswith(':'):
            grid = []
            i += 1
            while i < len(data) and data[i] and not data[i][0].isdigit():
                grid.append(data[i])
                i += 1
            grids.append(grid)
        else:
            i += 1

    while i < len(data):
        line = data[i]
        if 'x' in line and ':' in line:
            dims, indices = line.split(': ')
            r, c = map(int, dims.split('x'))
            idx_list = list(map(int, indices.split()))
            queries.append(([r, c], idx_list))
        i += 1

    return grids, queries

def solve(data: List[str]):
    grids, queries = parse(data)
    ans = 0

    for size, amount in queries:
        area = size[0] * size[1]
        needed_area = 3 * 3 * sum(amount)
        if area >= needed_area: ans += 1

    print(ans)


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
