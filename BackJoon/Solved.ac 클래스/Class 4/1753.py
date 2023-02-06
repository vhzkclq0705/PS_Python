# Gold 4 - 최단경로

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            total_dis = distance[node] + n_dis
            if total_dis < distance[n_node]:
                distance[n_node] = total_dis
                heappush(q, (total_dis, n_node))
    
    return

v, e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v + 1)]
distance = [0] + [sys.maxsize] * v

for _ in range(e):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))

dijkstra(s)

for i in distance[1:]:
    print(i if i != sys.maxsize else 'INF')