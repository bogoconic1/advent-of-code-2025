from typing import List

class CustomList:
    def __init__(self, values: List[int]):
        self.values = values

    def sum(self):
        return sum(self.values)

    def product(self):
        ans = 1
        for value in self.values:
            ans *= value
        return ans

def solve(data: List[str]):

    data = [x.split() for x in data]
    ans = 0

    # iterate columns
    for j in range(len(data[0])):
        values = []
        # last element is the operator
        for i in range(len(data) - 1):
            values.append(int(data[i][j]))
        custom_list = CustomList(values)
        if data[len(data) - 1][j] == "+":
            ans += custom_list.sum()
        else:
            ans += custom_list.product()

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
