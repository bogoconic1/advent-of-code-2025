from typing import List, Tuple
import re

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

def solve(data: List[str]):

    ans = 0
    # parse each line
    for line in data:
        pattern, combs, costs = parse_line(line)
        pattern = [1 if x == "#" else 0 for x in pattern]
        min_length = float('inf')

        for mask in range(1 << len(combs)):
            matched_pattern = [0]*len(pattern)
            num_used = 0
            for i in range(len(combs)):
                if mask & (1 << i):
                    num_used += 1
                    for idx in combs[i]:
                        matched_pattern[idx] = 1 - matched_pattern[idx]

            if matched_pattern == pattern:
                min_length = min(min_length, num_used)

        ans += min_length

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
