# Bronze 1 - 알고리즘 수업 - 피보나치 수 1

n = int(input())
dp = [1] * n

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1], n - 2)