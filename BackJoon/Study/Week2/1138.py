# Silver 2 - 한 줄로 서기

import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
t = list(range(1, n + 1))
ans = [0] * n

for i in range(n):
    ans[t.pop(s[i]) - 1] = i + 1

print(*ans)