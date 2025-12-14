from typing import List, Tuple
from collections import defaultdict
from heapq import heappush_max, heappop_max
from copy import deepcopy
from pprint import pprint

N_NEIGHBORS_PER_POINT = 4

def euclidean_distance(point1: Tuple[int, int, int], point2: Tuple[int, int, int]):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5

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

class Node:
    def __init__(self, point: Tuple[int, int, int], left: 'Node', right: 'Node', axis: int):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis

class KDTree:
    def __init__(self, points: List[Tuple[int, int, int]]):
        self.points = points
        self.n_dim = len(points[0])
        self.root = self.build(points, 0)

    def build(self, points: List[Tuple[int, int, int]], depth: int):
        if not points:
            return None
        points.sort(key=lambda x: x[depth])
        mid = len(points) // 2
        next_depth = (depth + 1) % self.n_dim
        return Node(points[mid], self.build(points[:mid], next_depth), self.build(points[mid+1:], next_depth), depth)

    def query(self, point: Tuple[int, int, int], k: int):
        heap = []

        def search(node: Node, depth: int):
            if node is None:
                return
            dist = euclidean_distance(point, node.point)
            if len(heap) < k:
                heappush_max(heap, (dist, node.point))
            else:
                # we need to kick out the highest distance point
                if dist < heap[0][0]:
                    heappop_max(heap)
                    heappush_max(heap, (dist, node.point))
            
            if point[node.axis] < node.point[node.axis]: 
                first, second = node.left, node.right
            else:
                first, second = node.right, node.left
            search(first, (depth + 1) % self.n_dim)
            if len(heap) < k or abs(point[node.axis] - node.point[node.axis]) < heap[0][0]:
                search(second, (depth + 1) % self.n_dim)

        search(self.root, 0)
        return heap # exactly k elements [distance, point]


def solve(data: List[str]):

    data = [[int(y) for y in x.split(",")] for x in data]
    num_components = len(data)

    tree = KDTree(deepcopy(data))

    point2idx = {tuple(point): i for i, point in enumerate(data)}

    # maintain a max heap of distances
    distances = []
    for i in range(len(data)):
        points = tree.query(data[i], N_NEIGHBORS_PER_POINT)
        for distance, point in points:
            distances.append((distance, i, point2idx[tuple(point)]))

    distances.sort(key=lambda x: x[0])

    uf = UnionFind(len(data))

    for distance, i, j in distances:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            num_components -= 1
            if num_components == 1:
                last_value = data[i][0] * data[j][0]
                break

    print(last_value)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
