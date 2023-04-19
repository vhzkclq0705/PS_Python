# LEVEL 2

def solution(n):
    if n < 4:
        return n
    dp = [0, 1, 2, 3] + [0] * (n - 3)
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n] % 1234567