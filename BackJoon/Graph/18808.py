# Gold 3 - 스티커 붙이기

import sys
input = sys.stdin.readline

def rotate(s, n):
    tmp = []

    for x, y in s:
        tmp.append((y, n - 1 - x))
    
    return tmp

def check(board, sticker, x, y, n, m):
    for dx, dy in sticker:
        nx = x + dx
        ny = y + dy

        if 0 > nx or nx >= n or 0 > ny or ny >= m or board[nx][ny] == 1:
            return False
    
    return True
            
n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
stickers = []
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(r)]
    p = []

    for x in range(r):
        for y in range(c):
            if s[x][y] == 1:
                p.append((x, y))

    stickers.append((p, r, c))

for sticker in stickers:
    flag = False
    s, r, c = sticker
    for i in range(4):
        if i > 0:
            s = rotate(s, r)
            r, c = c, r

        for x in range(n):
            for y in range(m):
                if check(board, s, x, y, n, m):
                    for dx, dy in s:
                        nx = x + dx
                        ny = y + dy

                        board[nx][ny] = 1
                    ans += len(s)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        continue

print(ans)