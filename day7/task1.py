from typing import List

def solve(data: List[str]):

    M = len(data)
    N = len(data[0])
    ans = 0

    S_pos = data[0].index("S")
    beams = set([S_pos])
    for i in range(1, M):
        new_beams = set()
        for beam in beams:
            if data[i][beam] == "^":
                # the edge case # ^^ cannot happen
                # also edge case ^ at leftmost and rightmost cannot happen
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                ans += 1
            else:
                new_beams.add(beam)

        beams = new_beams

    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(data)
