# Silver 3 - 진우의 달 여행 (Small)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * m for _ in range(n)] for _ in range(3)]
ans = sys.maxsize

for z in range(3):
    for y in range(m):
        dp[z][0][y] = board[0][y]

for x in range(1, n):
    for y in range(m):
        if y == 0:
            dp[0][x][y] = dp[1][x - 1][y]
            dp[1][x][y] = dp[0][x - 1][y + 1]
            dp[2][x][y] = min(dp[0][x - 1][y + 1], dp[1][x - 1][y])
        elif y == m - 1:
            dp[0][x][y] = min(dp[1][x - 1][y], dp[2][x - 1][y - 1])
            dp[1][x][y] = dp[2][x - 1][y - 1]
            dp[2][x][y] = dp[1][x - 1][y]
        else:
            dp[0][x][y] = min(dp[1][x - 1][y], dp[2][x - 1][y - 1])
            dp[1][x][y] = min(dp[0][x - 1][y + 1], dp[2][x - 1][y - 1])
            dp[2][x][y] = min(dp[0][x - 1][y + 1], dp[1][x - 1][y])

        for z in range(3):
            dp[z][x][y] += board[x][y]

for z in range(3):
    ans = min(ans, min(dp[z][-1]))

print(ans)