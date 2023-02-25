# Silver 1 - 쉬운 최단거리

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
board = []
x, y = 0, 0

for i in range(n):
    s = list(map(int, input().split()))
    board.append(s)
    for j in range(m):
        if s[j] == 2:
            x, y = i, j

visited = [[0] * m for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

bfs(x, y)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for i in visited:
    print(*i)