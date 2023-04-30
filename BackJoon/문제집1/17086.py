# Silver 2 - 아기 상어 2

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y]+1
                q.append((nx, ny))

print(max(max(i) for i in board) - 1)