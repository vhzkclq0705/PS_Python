# Silver 2 - 부분수열의 합

import sys
input = sys.stdin.readline

def dfs(idx, total):
    if idx == n:
        return
    
    for i in range(idx, n):
        total += nums[i]
        if total == s:
            global ans
            ans += 1

        dfs(i + 1, total)
        total -= nums[i]

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

dfs(0, 0)

print(ans)