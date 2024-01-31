# Gold 4 - Puyo Puyo

from collections import deque
import sys
input = sys.stdin.readline

def move():
    for x, y in boom:
        for i in range(x, 0, -1):
            board[i][y] = board[i - 1][y]
        board[0][y] = '.'

def bfs(x, y):
    q = deque([(x, y)])
    visited.add((x, y))
    tmp = [(x, y)]

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == board[x][y] and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
                tmp.append((nx, ny))

    if len(tmp) > 3:
        for x, y in tmp:
            board[x][y] = '.'
            boom.append((x, y))
    
board = [list(input().rstrip()) for _ in range(12)]
ans = 0

while True:
    visited = set()
    boom = []

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and (i, j) not in visited:
                bfs(i, j)

    if not boom:
        break

    move()
    ans += 1

print(ans)