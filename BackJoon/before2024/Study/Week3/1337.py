# Silver 4 - 올바른 배열

import sys
input = sys.stdin.readline

n = int(input())
s = sorted([int(input()) for _ in range(n)])
cnt = 5

for i in s:
    cnt = min(cnt, 5 - len(set(range(i, i + 5)) & set(s)))

print(cnt)