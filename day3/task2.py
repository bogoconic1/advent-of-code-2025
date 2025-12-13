from typing import List

def solve(batteries: List[str]):
    ans = 0
    for battery in batteries:
        dp = [0]*12
        for char in battery:
            digit = int(char)
            for i in range(11, 0, -1):
                dp[i] = max(dp[i], dp[i-1] * 10 + digit)
            dp[0] = max(dp[0], digit)

        ans += dp[11]
            
    print(ans)

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    batteries = open(os.path.join(dir_path, "input.txt"), "r").read().splitlines()
    solve(batteries)
