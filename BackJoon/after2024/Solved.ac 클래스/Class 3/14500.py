# Gold 4 - 테트로미노

import sys
input = sys.stdin.readline

def dfs(x, y, cnt, total):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if cnt == 2:
                dfs(x, y, cnt + 1, total + board[nx][ny])
            dfs(nx, ny, cnt + 1, total + board[nx][ny])
            visited[nx][ny] = False

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = max(map(max, board))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)