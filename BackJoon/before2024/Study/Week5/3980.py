# Gold 5 - 선발 명단

import sys
input = sys.stdin.readline

def bt(p, depth):
    if depth == 11:
        ans.append(sum(p))
        return
    
    for i in range(11):
        if not visited[i] and s[i][depth] > 0:
            visited[i] = True
            p[depth] = s[i][depth]
            bt(p, depth + 1)
            visited[i] = False
            p[depth] = 0

for _ in range(int(input())):
    s = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    p = [0] * 11
    ans = []

    bt(p, 0)
    print(max(ans))