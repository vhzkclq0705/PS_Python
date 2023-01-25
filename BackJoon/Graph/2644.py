# Silver 2 - 촌수계산

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, a, b):
    q = deque([a])
    visited[a] = 0

    while q:
        n = q.popleft()

        for i in graph[n]:
            if visited[i] == -1:
                visited[i] = visited[n] + 1
                q.append(i)

n = int(input())
a, b = map(lambda x: int(x) - 1, input().split())
m = int(input())
graph = [[] for _ in range(n)]
visited = [-1] * n

for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(graph, visited, a, b)
print(visited[b])