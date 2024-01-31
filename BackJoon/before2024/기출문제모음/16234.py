# Gold 5 - 인구 이동

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    union = [(x, y)]

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(country[x][y] - country[nx][ny]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                union.append((nx, ny))
    
    return union

def move(union):
    union = list(union)
    l = len(union)
    total = 0

    for x, y in union:
        total += country[x][y]
    
    for x, y in union:
        country[x][y] = total // l

n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i, j)
                if len(union) > 1:
                    flag = False
                    move(union)
    
    if flag:
        print(ans)
        break
    
    ans += 1