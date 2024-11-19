# BOJ
# S5 - 2018(수들의 합 5)

import sys
input = sys.stdin.readline

n = int(input())
l, r = 0, 0
total = 0
ans = 0

while r <= n:
    if total < n:
        r += 1
        total += r
    elif total > n:
        total -= l
        l += 1
    else:
        ans += 1
        r += 1
        total += r

print(ans)