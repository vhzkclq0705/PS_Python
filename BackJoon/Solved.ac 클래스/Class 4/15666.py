# Silver 2 - N과 M (12)

def dfs(depth):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(depth, len(s)):
        ans.append(s[i])
        dfs(i)
        ans.pop()

n, m = map(int, input().split())
s = sorted(set(map(int, input().split())))
ans = []

dfs(0)