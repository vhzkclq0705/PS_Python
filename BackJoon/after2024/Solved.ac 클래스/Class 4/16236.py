# Gold 3 - 아기상어

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    fish = []
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= level:
                visited[nx][ny] = True
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

                if 0 < board[nx][ny] < level:
                    fish.append((distance[nx][ny], nx, ny))
                    
    return sorted(fish, reverse=True)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
shark = [0, 0]
level, exp = 2, 0
ans = 0

for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            shark[0], shark[1] = x, y

while True:
    fish = bfs(shark[0], shark[1])
    if not fish:
        print(ans)
        break

    dis, x, y = fish.pop()
    ans += dis
    board[shark[0]][shark[1]] = 0
    board[x][y] = 0
    shark[0], shark[1] = x, y
    exp += 1
    if exp == level:
        level += 1
        exp = 0