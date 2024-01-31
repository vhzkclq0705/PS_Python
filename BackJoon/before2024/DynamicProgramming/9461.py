# Silver 3 - 파도반 수열

dp = [1] * 101

for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    print(dp[int(input())])