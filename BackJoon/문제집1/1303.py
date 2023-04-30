# Silver 1 - 전쟁-전투

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
w, b = 0, 0

def bfs(x, y, team):
    visited[x][y] = True
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == team:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return cnt ** 2

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if board[i][j] == 'W':
                w += bfs(i, j, 'W')
            else:
                b += bfs(i, j, 'B')

print(w, b)