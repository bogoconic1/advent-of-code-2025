from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def solve(data: List[str]):

    uf = UnionFind(len(data))

    # preprocess distances
    distances = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            xi, yi, zi = data[i].split(",")
            xi, yi, zi = int(xi), int(yi), int(zi)
            xj, yj, zj = data[j].split(",")
            xj, yj, zj = int(xj), int(yj), int(zj)
            # euclidean distance
            distance = ((xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2) ** 0.5
            distances.append((i, j, distance))

    distances.sort(key=lambda x: x[2])

    for i, j, distance in distances[:1000]:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)

    group_size = defaultdict(int)
    for i in range(len(data)):
        group_size[uf.find(i)] += 1

    highest_sizes = sorted(group_size.values(), reverse=True)[:3]
    print(highest_sizes[0] * highest_sizes[1] * highest_sizes[2])

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
