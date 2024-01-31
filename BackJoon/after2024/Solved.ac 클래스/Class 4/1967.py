# Gold 4 - 트리의 지름

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance = [sys.maxsize] * n
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            t_dis = distance[node] + n_dis
            if t_dis < distance[n_node]:
                distance[n_node] = t_dis
                heappush(q, (t_dis, n_node))

    MAX = max(distance)
    return MAX, distance.index(MAX)

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, t = map(int, input().split())
    graph[a - 1].append((t, b - 1))
    graph[b - 1].append((t, a - 1))

_, idx = dijkstra(0)
v, _ = dijkstra(idx)

print(v)