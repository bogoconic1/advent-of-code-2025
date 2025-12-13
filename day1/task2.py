from typing import List
def solve(moves: List[str]):

    pos = 50
    ans = 0
    for move in moves:
        shift = int(move[1:])
        if move[0] == "L":
            start = pos // 100
            if pos % 100 == 0: start -= 1
            pos -= shift
            end = pos // 100
            if pos % 100 == 0: end -= 1
        else:
            start = pos // 100
            # if pos % 100 == 0: start += 1
            pos += shift
            end = pos // 100
            # if pos % 100 == 0: end += 1


        ans += abs(end - start)

        # edge case: if start is 0
        # edge case: if end is 0

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    moves = open(os.path.join(dir_path, "input.txt"), "r").readlines()
    solve(moves)
