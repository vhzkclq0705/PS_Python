# Bronze 1 - 알고리즘 수업 - 피보나치 수 1

def fib_Recu(n):
    if n < 3:
        return 1

    return fib_Recu(n - 1) + fib_Recu(n - 2)

def fib_DP(n):
    dp = [1] * n
    cnt = 0
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1
    
    return cnt

n = int(input())
print(fib_Recu(n), fib_DP(n))