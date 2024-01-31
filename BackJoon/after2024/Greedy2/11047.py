# Silver 4 - 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0

for i in range(n - 1, -1, -1):
    if coins[i] <= k:
        ans += k // coins[i]
        k %= coins[i]

print(ans)