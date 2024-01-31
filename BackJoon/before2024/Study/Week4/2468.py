# Silver 1 - 안전 영역

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, x, y, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                q.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1

for i in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and not visited[x][y]:
                bfs(graph, visited, x, y, i)
                cnt += 1
    
    if cnt == 0:
        break
    ans = max(ans, cnt)

print(ans)