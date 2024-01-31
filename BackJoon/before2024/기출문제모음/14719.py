# Gold 5 - 빗물

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, w - 1):
    left = max(block[:i])
    right = max(block[i + 1:])
    low = min(left, right)

    if low > block[i]:
        ans += low - block[i]

print(ans)