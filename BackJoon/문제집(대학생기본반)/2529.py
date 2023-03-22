# Silver 1 - 부등호

import sys
input = sys.stdin.readline

def check(i, j, k):
    return i < j if k == '<' else i > j

def dfs(depth, tmp):
    global ans_max, ans_min
    if depth == n + 1:
        if not ans_min:
            ans_min = tmp
        else:
            ans_max = tmp
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(tmp[-1], str(i), s[depth - 1]):
                visited[i] = True
                dfs(depth + 1, tmp + str(i))
                visited[i] = False

n = int(input())
s = list(input().rstrip().split())
visited = [False] * 10
ans_max, ans_min = "", ""

dfs(0, "")

print(ans_max)
print(ans_min)