# Silver 2 - 창고 다각형

import sys
input = sys.stdin.readline

n = int(input())
board = []
MAX_L, MAX_H = 0, 0
ans = 0

for _ in range(n):
    l, h = map(int, input().split())
    board.append([l, h, True])

    if h > MAX_H:
        MAX_L = l
        MAX_H = h

board.sort()
idx = board.index([MAX_L, MAX_H, True])

for i in range(idx + 1):
    for j in range(i + 1, idx + 1):
        if board[i][2] and board[j][1] >= board[i][1]:
            ans += (board[j][0] - board[i][0]) * board[i][1]
            break
        elif board[j][1] < board[i][1]:
            board[j][2] = False

for i in range(n - 1, idx - 1, -1):
    for j in range(i - 1, idx - 1, -1):
        if board[i][2] and board[j][1] >= board[i][1]:
            ans += (board[i][0] - board[j][0]) * board[i][1]
            break
        elif board[j][1] < board[i][1]:
            board[j][2] = False

print(ans + MAX_H)