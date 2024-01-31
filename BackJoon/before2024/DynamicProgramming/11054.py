# Gold 4 - 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[j] + 1, dp[i])

for i in range(1, n):
    for j in range(i):
        if s[i] < s[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))