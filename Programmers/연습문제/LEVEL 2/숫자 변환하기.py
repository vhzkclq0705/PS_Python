# LEVEL 2

def solution(x, y, n):
    dp = [1e9] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y + 1):
        if dp[y] != 1e9:
            return dp[y]
        
        for j in (i + n, i * 2, i * 3):
            if j > y:
                continue
            dp[j] = min(dp[i] + 1, dp[j])
    
    return -1 if dp[y] == 1e9 else dp[y]