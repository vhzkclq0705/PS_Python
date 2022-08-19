import sys
input = sys.stdin.readline

n = input().rstrip()
l = len(n) + 1
dp = [0] * l
dp[0] = dp[1] = 1

if n[0] == '0':
    print(0)
    exit()

for i in range(2, l):
    if int(n[i - 1]) > 0:
        dp[i] += dp[i - 1]
    if 10 <= int(n[i - 2] + n[i - 1]) <= 26:
        dp[i] += dp[i - 2]    

print(dp[-1] % 1000000)