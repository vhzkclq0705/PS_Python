# Gold 5 - 파이프 옮기기 1

# 재귀 이용 - 시간초과
# import sys
# input = sys.stdin.readline

# def bfs(x, y, d):
#     if x >= n or y >= n or board[x][y] == 1:
#         return
#     if d == 2 and (board[x - 1][y] == 1 or board[x][y - 1] == 1):
#         return
#     if x == n - 1 and y == n - 1:
#         global ans
#         ans += 1
#         return
    
#     if d == 0: # 가로
#         bfs(x, y + 1, 0)
#         bfs(x + 1, y + 1, 2)
#     elif d == 1:
#         bfs(x + 1, y, 1)
#         bfs(x + 1, y + 1, 2)
#     else:
#         bfs(x, y + 1, 0)
#         bfs(x + 1, y, 1)
#         bfs(x + 1, y + 1, 2)

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# ans = 0

# bfs(0, 1, 0)
# print(ans)

# DP
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * (n) for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for y in range(2, n):
    if board[0][y] == 0:
        dp[0][0][y] = dp[0][0][y - 1]

for x in range(1, n):
    for y in range(1, n):
        if board[x][y] == 0:
            dp[0][x][y] += dp[0][x][y - 1] + dp[2][x][y - 1]
            dp[1][x][y] += dp[1][x - 1][y] + dp[2][x - 1][y]
            if board[x - 1][y] == 0 and board[x][y - 1] == 0:
                dp[2][x][y] += dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]

print(sum(dp[i][-1][-1] for i in range(3)))