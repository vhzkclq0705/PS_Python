# Gold 4 - 부분합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
start, end, SUM = 0, 0, 0
ans = n + 1

while True:
    if SUM >= m:
        ans = min(ans, end - start)
        SUM -= s[start]
        start += 1
    elif end == n:
        break
    elif SUM < m:
        SUM += s[end]
        end += 1

print(ans if ans != n + 1 else 0)