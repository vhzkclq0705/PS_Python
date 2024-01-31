# Gold 5 - 로봇 청소기

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, d):
    q = deque([(x, y)])
    board[x][y] = 2
    cnt = 1

    while q:
        x, y = q.popleft()

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                cnt += 1
                break
        else:
            nx = x - dx[d]
            ny = y - dy[d]

            if board[nx][ny] == 1:
                return cnt
            else:
                q.append((nx, ny))
    
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(bfs(r, c, d))