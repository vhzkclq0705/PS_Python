# Gold 5 - 로봇 청소기

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, d):
    q = deque([(x, y)])
    board[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + p[d][0]
            ny = y + p[d][1]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
                break
        else:
            nx = x - p[d][0]
            ny = y - p[d][1]

            if board[nx][ny] == -1:
                return cnt
            else:
                q.append((nx, ny))
    
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(lambda x: int(x) * -1, input().split())) for _ in range(n)]
p = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(bfs(r, c, d))