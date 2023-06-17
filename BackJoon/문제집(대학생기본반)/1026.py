# Silver 4 - 보물

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
ans = 0

for i in range(n):
    ans += a[i] * b[i]

print(ans)