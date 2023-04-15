# LEVEL 2

from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    q = deque([])
    visited = set()
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
    
    while q:
        x, y, cnt = q.popleft()
        if board[x][y] == 'G':
            return cnt
        if (x, y) in visited:
            continue
        visited.add((x, y))
    
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                nx += dx
                ny += dy
            q.append((nx - dx, ny - dy, cnt + 1))
    
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))