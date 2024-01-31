# Gold 5 - 전깃줄

import sys
input = sys.stdin.readline

n = int(input())
s = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [1] * n

for i in range(n):
    for j in range(i):
        if s[i][1] > s[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))