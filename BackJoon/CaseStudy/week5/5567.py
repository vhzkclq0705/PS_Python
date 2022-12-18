import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
q = deque()

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q.append([1, 0])
    visited[1] = True
    ans = 0

    while q:
        v, cnt = q.popleft()

        if cnt <= 2:
            ans += 1

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt + 1))

    return ans - 1

print(bfs())