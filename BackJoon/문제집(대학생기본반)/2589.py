# GOlD 5 - 보물섬

from collections import deque
import sys
input = sys.stdin.readline

def check(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L':
            cnt += 1
    
    return cnt < 3

def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y, 0)])

    while q:
        x, y, dis = q.popleft()
        global ans
        ans = max(ans, dis)

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))
    
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'L' and check(i, j):
            bfs(i, j)

print(ans)