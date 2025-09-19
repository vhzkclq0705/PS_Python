from collections import deque

def crain(matrix, n, m, req):
    temp = matrix
    for i in range(n):
        for j in range(m):
            if temp[i][j] == req:
                temp[i][j] = 'x'
    return temp

def lift(matrix, n, m, req):
    temp = matrix
    q = deque()
    visited = [[False] * m for i in range(n)]
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for i in range(n):
        for j in range(m):
            if 0 < i < n - 1 and 0 < j < m - 1:
                continue
            if temp[i][j] == 'x':
                q.append((i, j))
            elif temp[i][j] == req:
                temp[i][j] = ' '
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if temp[nx][ny] == 'x':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif temp[nx][ny] == req:
                    temp[nx][ny] = ' '
                    visited[nx][ny] = True
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == ' ':
                temp[i][j] = 'x'
        
    return temp

def solution(storage, requests):
    answer = 0
    matrix = [list(i) for i in storage]
    n = len(storage)
    m = len(storage[0])
    
    for req in requests:
        if len(req) == 1:
            matrix = lift(matrix, n, m, req)
        else:
            matrix = crain(matrix, n, m, req[0])
        
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                answer += 1
    
    return answer