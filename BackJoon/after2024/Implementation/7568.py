# Silver 5 - 덩치

import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
rank = sorted(people, reverse=True)

for px, py in people:
    ans = 1
    for rx, ry in rank:
        if px < rx and py < ry:
            ans += 1

    print(ans, end=' ')