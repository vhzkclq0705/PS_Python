# Silver 5 - 올림픽

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
rank = []

for _ in range(n):
    c, g, s, b = map(int, input().split())
    rank.append((g, s, b))

    if c == k:
        tmp = (g, s, b)

rank.sort(reverse=True)

for i in range(n):
    if rank[i] == tmp:
        print(i + 1)
        break