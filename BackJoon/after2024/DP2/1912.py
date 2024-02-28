# Silver 2 - 연속합

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] + [0] * (n - 1)

for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))