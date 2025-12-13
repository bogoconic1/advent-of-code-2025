from typing import List
from pprint import pprint

def solve(data: List[str]):
    ans = 0
    current_stream = 0
    current_op = ""

    # pad to max length first
    max_length = max(len(row) for row in data)
    for i in range(len(data)):
        data[i] += " " * (max_length - len(data[i]))

    # iterate columns
    for j in range(len(data[0])):
        value = None
        # last element is the operator
        for i in range(len(data) - 1):
            if data[i][j].isdigit():
                if value is None:
                    value = int(data[i][j])
                else:
                    value = 10 * value + int(data[i][j])

        if value is None: continue

        if data[len(data) - 1][j] in ["+", "*"]:
            ans += current_stream
            current_stream = value
            current_op = data[len(data) - 1][j]
        else:
            if current_op == "+":
                current_stream += value
            else:
                current_stream *= value

    ans += current_stream
    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
