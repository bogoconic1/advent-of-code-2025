from typing import List, Tuple
import re
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

# this is AI generated
def parse_line(line: str) -> Tuple[str, List[List[int]], List[int]]:
    match = re.match(r'\[(.*?)\]\s*(.*)\s*\{(.*?)\}', line.strip())
    
    pattern_str = match.group(1)
    middle_str = match.group(2)
    final_str = match.group(3)

    middle_parts = []
    for group in re.findall(r'\((.*?)\)', middle_str):
        # Convert "1,2,3" -> [1, 2, 3] and "3" -> [3]
        nums = list(map(int, group.split(',')))
        middle_parts.append(nums)

    final_list = [int(x) for x in final_str.split(',') if x.strip()]
    
    return pattern_str, middle_parts, final_list

# time limit exceeded: O(274 ^ 13)
def branch(index: int, ops: int, combs: List[List[int]], current_costs: List[int]):

    if index == len(combs):
        return ops if current_costs == [0]*len(current_costs) else float('inf')

    ans = float('inf')
    iterations = min(current_costs)

    for i in range(iterations+1):
        for idx in combs[index]:
            current_costs[idx] -= i
        ans = min(ans, branch(index + 1, ops + i, combs, current_costs))
        for idx in combs[index]:
            current_costs[idx] += i

    return ans

def system_solver(combs: List[List[int]], costs: List[int]):
    """
    x = [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
    y = [3, 5, 4, 7]

    We minimize
    x0 + x1 + x2 + x3 + x4 + x5

    subject to the constraints:
    x4 + x5 = 3 -> value 0
    x1 + x5 = 5 -> value 1
    x2 + x3 + x4 = 4 -> value 2
    x0 + x1 + x3 = 7 -> value 3

    milp(c, *, integrality=None, bounds=None, constraints=None, options=None)

    so constraint matrix:
    [[0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 1, 1, 0],
     [1, 1, 0, 1, 0, 0]]

    integrality:
    [1, 1, 1, 1, 1, 1] : all integer within bounds

    bounds:
    [0, inf)
    """
    constraints = np.zeros((len(costs), len(combs)))
    for i, group in enumerate(combs):
        for idx in group:
            constraints[idx][i] = 1

    constraints = LinearConstraint(constraints, lb=costs, ub=costs)
    bounds = Bounds(lb=0, ub=float("inf"))
    integrality = np.ones(len(combs))
    result = milp(c=np.ones(len(combs)), constraints=constraints, bounds=bounds, integrality=integrality)
    return result.fun


def solve(data: List[str]):

    ans = 0
    # parse each line
    for line in data:
        pattern, combs, costs = parse_line(line)
        line_ans = system_solver(combs, costs)
        ans += line_ans

    print(ans)
    
if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
