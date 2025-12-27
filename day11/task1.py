from typing import List, Dict
from collections import deque, defaultdict

def parse(data: List[str]) -> Dict[str, List[str]]:
    graph = {}
    for line in data:
        node, neighbors = line.split(": ")
        graph[node] = neighbors.split()
    return graph

def solve(data: List[str]):
    graph = parse(data)
    dp = defaultdict(lambda: 0)
    dp['you'] = 1

    # run a first BFS to check those unreachable nodes
    reachable = set()
    queue = deque()
    queue.append('you')
    while queue:
        node = queue.popleft()
        if node == "out": continue
        reachable.add(node)
        for neighbor in graph[node]:
            if neighbor not in reachable:
                queue.append(neighbor)
    
    ind = defaultdict(int)
    for node in reachable:
        for neighbor in graph[node]:
            ind[neighbor] += 1

    # topo sort
    queue = deque()
    queue.append('you')
    while queue:
        node = queue.popleft()
        if node == "out":
            continue
        for neighbor in graph[node]:
            dp[neighbor] += dp[node]
            ind[neighbor] -= 1
            if ind[neighbor] == 0:
                queue.append(neighbor)

    print(dp['out'])


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
