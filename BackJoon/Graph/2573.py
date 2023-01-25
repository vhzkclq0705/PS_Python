# Gold 4 - 빙산

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, n, m, visited):
    melt = []
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        cnt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    cnt += 1
        
        if cnt > 0:
            melt.append((x, y, cnt))
    
    for x, y, cnt in melt:
        graph[x][y] = max(0, graph[x][y] - cnt)
    
    return 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0 and not visited[x][y]:
                cnt += bfs(x, y, n, m, visited)
            if cnt > 1:
                print(year)
                exit()
    
    if cnt == 0:
        print(0)
        break

    year += 1