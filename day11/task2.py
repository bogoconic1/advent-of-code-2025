from typing import List, Dict
from collections import deque, defaultdict

def parse(data: List[str]) -> Dict[str, List[str]]:
    graph = {}
    for line in data:
        node, neighbors = line.split(": ")
        graph[node] = neighbors.split()
    return graph

def traverse(graph: Dict[str, List[str]], start: str, end: str) -> int:
    dp = defaultdict(lambda: 0)
    dp[start] = 1

    # run a first BFS to check those unreachable nodes
    reachable = set([start])
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node == end or node == "out": continue
        assert node != "out"
        for neighbor in graph[node]:
            if neighbor not in reachable:
                queue.append(neighbor)
                reachable.add(neighbor)
    
    ind = defaultdict(int)
    for node in reachable - {"out"}:
        for neighbor in graph[node]:
            ind[neighbor] += 1

    # topo sort
    queue = deque()
    seen = set([start])
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node == end or node == "out": continue
        for neighbor in graph[node]:
            dp[neighbor] += dp[node]
            ind[neighbor] -= 1
            if ind[neighbor] == 0:
                queue.append(neighbor)
                seen.add(neighbor)

    return dp[end]

def solve(data: List[str]):
    graph = parse(data)

    svr2dac = traverse(graph, 'svr', 'dac')
    dac2fft = traverse(graph, 'dac', 'fft')
    fft2out = traverse(graph, 'fft', 'out')


    svr2fft = traverse(graph, 'svr', 'fft')
    fft2dac = traverse(graph, 'fft', 'dac')
    dac2out = traverse(graph, 'dac', 'out')

    ans = svr2dac * dac2fft * fft2out + svr2fft * fft2dac * dac2out
    print(ans)


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
