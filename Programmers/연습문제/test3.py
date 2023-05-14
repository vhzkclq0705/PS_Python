from collections import deque

def display(board, n):
    for i in range(n):
        board[i] = ''.join(board[i])
    return board

def solution(board, y, x):
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True
    q = deque([(y, x)])

    for i in range(n):
        board[i] = list(board[i])
    
    if board[x][y] == 'M':
        board[x][y] = 'X'
        return display(board, n)

    while q:
        x, y = q.popleft()
        cnt = 0
        tmp = []

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 'M':
                    cnt += 1
                else:
                    visited[nx][ny] = True
                    tmp.append((nx, ny))
                
        if cnt:
            board[x][y] = str(cnt)
            for nx, ny in tmp:
                visited[nx][ny] = False
        else:
            board[x][y] = 'B'
            for nx, ny in tmp:
                q.append((nx, ny))
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'E'

        display(board, n)

    return board



print(solution(['EEEEE', 'EEMEE', 'EEEEE', 'EEEEE'], 2, 0))
print(solution(['MME', 'EEE', 'EME'], 0, 0))