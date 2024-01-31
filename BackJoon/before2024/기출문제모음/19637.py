# Silver 3 - IF문 좀 대신 써줘

from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
cnt = [-1]

for _ in range(n):
    a, b = input().split()
    title.append(a)
    cnt.append(int(b))

for _ in range(m):
    print(title[bisect_left(cnt, int(input())) - 1])