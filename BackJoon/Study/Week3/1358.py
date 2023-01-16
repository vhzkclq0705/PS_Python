# Silver 4 - 하키

import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
players = [list(map(int, input().split())) for _ in range(p)]
r = h // 2
cnt = 0

for p in players:
    if r ** 2 >= (x - p[0]) ** 2 + (y + r - p[1]) ** 2:
        cnt += 1
    elif r ** 2 >= (x + w - p[0]) ** 2 + (y + r - p[1]) ** 2:
        cnt += 1
    elif x <= p[0] <= x + w and y <= p[1] <= y + h:
        cnt += 1

print(cnt)