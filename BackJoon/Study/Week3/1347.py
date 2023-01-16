# Silver 3 - 미로 만들기

import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
d = [3, 2, 4, 1] # 남, 서, 북, 동
p = [(0, 0)]
now = 0

for i in s:
    if i == 'R':
        now += 1
    elif i == 'L':
        now -= 1
    else:
        now = (abs(now) % 4) * -1 if now < 0 else now % 4
        x, y = p[-1]
        if d[now] == 1:
            p.append((x, y + 1))
        elif d[now] == 2:
            p.append((x, y - 1))
        elif d[now] == 3:
            p.append((x + 1, y))
        else:
            p.append((x - 1, y))

p.sort(key=lambda x: (x[0], x[1]))
min_Row = p[0][0]
row = p[-1][0] - p[0][0] + 1
p.sort(key=lambda x: (x[1], x[0]))
min_Col = p[0][1]
col = p[-1][1] - p[0][1] + 1

maze = [['#'] * col for _ in range(row)]

for x, y in p:
    maze[x - min_Row][y - min_Col] = '.'

for i in maze:
    print(*i, sep='')