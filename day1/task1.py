import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    moves = open(os.path.join(dir_path, "input.txt"), "r").readlines()
    pos = 50
    ans = 0
    for move in moves:
        shift = int(move[1:])
        if move[0] == "L":
            pos -= shift
        else:
            pos += shift
        if pos % 100 == 0:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
