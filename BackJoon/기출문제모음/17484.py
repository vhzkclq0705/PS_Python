# Silver 3 - 진우의 달 여행 (Small)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[601] + list(map(int, input().split())) + [601] for _ in range(n)]
dp = [[[601] * 3 for _ in range(m + 2)] for _ in range(n)]

for i in range(n):
    if i == 0:
        for j in range(m + 2):
            for k in range(3):
                dp[i][j][k] = s[i][j]
    else:
        for j in range(1, m + 1):
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + s[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + s[i][j]
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + s[i][j]

print(min(map(min, dp[-1])))