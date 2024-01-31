# Silver 3 - N과 M (8)

def dfs(depth):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(depth, n):
        ans.append(s[i])
        dfs(i)
        ans.pop()
    
n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
ans = []

dfs(0)