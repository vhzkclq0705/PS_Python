# Silver 2 - 헌내기를 친구가 필요해

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    ans = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
           nx = x + dx
           ny = y + dy

           if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 'X':
                if graph[nx][ny] == 'P':
                    ans += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return ans if ans else 'TT'

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            print(bfs(i, j))
            exit()