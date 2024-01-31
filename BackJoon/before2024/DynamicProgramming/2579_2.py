# Silver 3 - 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
scores = [0] * 301
dp = [0] * 301

for i in range(n):
    scores[i] = int(input())

dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0], scores[1]) + scores[2]

for i in range(3, n):
    dp[i] = max(dp[i - 3] + scores[i - 1], dp[i - 2]) + scores[i]

print(dp[n - 1])