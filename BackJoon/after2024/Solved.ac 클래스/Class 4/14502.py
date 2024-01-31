# Gold 4 - 연구소

import sys, copy
from collections import deque
input = sys.stdin.readline

def spread(new_board):
    q = deque(virus)
    cnt = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and new_board[nx][ny] == 0:
                new_board[nx][ny] = 2
                q.append((nx, ny))
    
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                cnt += 1

    return cnt

def dfs(depth, idx):
    global ans
    if depth == 3:
        new_board = copy.deepcopy(board)
        for x, y in wall:
            new_board[x][y] = 1

        ans = max(ans, spread(new_board))
        return

    for i in range(idx, len(safe_area)):
        wall.append(safe_area[i])
        dfs(depth + 1, i + 1)
        wall.pop()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
safe_area = []
virus = []
wall = []
ans = 0

for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            safe_area.append((x, y))
        elif board[x][y] == 2:
            virus.append((x, y))

dfs(0, 0)
print(ans)