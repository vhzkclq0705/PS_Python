import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())
dp = {}
dp[0] = 1

def a(i):
    if i not in dp:
        dp[i] = a(i // p) + a(i // q)
    
    return dp[i]

print(a(n))