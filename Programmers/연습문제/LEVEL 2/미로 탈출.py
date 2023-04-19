# LEVEL 2

from collections import deque

def bfs(maps, n, m, sX, sY, eX, eY):
    visited = [[False] * m for _ in range(n)]
    q = deque([(sX, sY, 0)])
    visited[sX][sY] = True
    
    while q:
        x, y, dis = q.popleft()
        if x == eX and y == eY:
            return dis
        
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))
    
    return -1

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sX, sY = i, j
            elif maps[i][j] == 'E':
                eX, eY = i, j
            elif maps[i][j] == 'L':
                lX, lY = i, j
    
    s_l = bfs(maps, n, m, sX, sY, lX, lY)
    l_e = bfs(maps, n, m, lX, lY, eX, eY)
    
    return -1 if s_l == -1 or l_e == -1 else s_l + l_e