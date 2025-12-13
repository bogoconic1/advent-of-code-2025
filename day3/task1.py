from typing import List

def solve(batteries: List[str]):
    ans = 0
    for battery in batteries:
        dp = [0]*2
        for char in battery:
            digit = int(char)
            dp[1] = max(dp[1], dp[0] * 10 + digit)
            dp[0] = max(dp[0], digit)

        ans += dp[1]
            
    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    batteries = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(batteries)
