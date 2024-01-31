# Gold 5 - 숫자고르기

import sys
input = sys.stdin.readline

def dfs(v, first_item):
    visited[v] = True
    next_item = arr[v]

    if not visited[next_item]:
        dfs(next_item, first_item)
    elif visited[next_item] and next_item == first_item:
        ans.append(next_item)

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
ans = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(ans))
print(*sorted(ans), sep='\n')