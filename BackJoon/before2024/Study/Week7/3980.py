# Gold 5 - 선발 명단

import sys
input = sys.stdin.readline

def dfs(p, depth):
    global ans
    if depth == 11:
        ans = max(ans, sum(p))
        return

    for i in range(11):
        if not visited[i] and s[i][depth] > 0:
            visited[i] = True
            p[depth] = s[i][depth]
            dfs(p, depth + 1)
            visited[i] = False
            p[depth] = 0

for _ in range(int(input())):
    s = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    p = [0] * 11
    ans = 0

    dfs(p, 0)
    print(ans)
