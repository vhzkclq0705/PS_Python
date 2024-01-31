# Gold 4 - 미세먼지 안녕!

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def spread():
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                dust = board[x][y] // 5

                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        spread_dust[(nx, ny)] += dust
                        board[x][y] -= dust
    
    for k, v in spread_dust.items():
        board[k[0]][k[1]] += v

def upper_area(top):
    prev, d = 0, 1
    x, y = top, 1

    while True:
        nx = x + dxy[d][0]
        ny = y + dxy[d][1]

        if x == top and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d = (d - 1) % 4
            continue

        board[x][y], prev = prev, board[x][y]
        x, y = nx, ny

def lower_area(bottom):
    prev, d = 0, 1
    x, y = bottom, 1

    while True:
        nx = x + dxy[d][0]
        ny = y + dxy[d][1]

        if x == bottom and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d = (d + 1) % 4
            continue

        board[x][y], prev = prev, board[x][y]
        x, y = nx, ny

def purify():
    for x in range(2, r):
        if board[x][0] == -1:
            upper_area(x)
            lower_area(x + 1)

            for i in range(2):
                board[x][i] = i - 1
                board[x + 1][i] = i - 1
            break

r, c, t = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(r)]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(t):
    spread_dust = defaultdict(int)
    spread()
    purify()

print(sum(map(sum, board)) + 2)