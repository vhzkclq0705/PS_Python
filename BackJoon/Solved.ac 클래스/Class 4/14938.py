# Gold 4 - 서강그라운드

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
    h = []
    distance = [sys.maxsize] * n
    distance[start] = 0
    heappush(h, (0, start))

    while h:
        dis, node = heappop(h)

        if distance[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            t_dis = n_dis + distance[node]
            if t_dis < distance[n_node]:
                distance[n_node] = t_dis
                heappush(h, (t_dis, n_node))

    return sum([t[i] for i in range(n) if distance[i] <= m])

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [[] for _ in range(n)]
ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((l, b - 1))
    graph[b - 1].append((l, a - 1))

for i in range(n):
    ans = max(ans, dijkstra(i))

print(ans)