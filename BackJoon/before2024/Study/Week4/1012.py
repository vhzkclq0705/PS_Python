# Silver 2 - 유기농 배추

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                bfs(graph, x, y, n, m)
                cnt += 1
    
    print(cnt)