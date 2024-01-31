# Gold 5 - 뱀과 사다리 게임

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        v = q.popleft()
        if v == 100:
            return visited[-1] - 1

        for i in range(1, 7):
            x = v + i
            if x > 100:
                continue

            x = graph[v + i]

            if visited[x] == 0:
                visited[x] = visited[v] + 1
                q.append(x)

n, m = map(int, input().split())
graph = [i for i in range(101)]
visited = [0] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    graph[a] = b

print(bfs(1))