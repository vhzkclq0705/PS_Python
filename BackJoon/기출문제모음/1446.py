# Silver 1 - 지름길

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance = [0] + [sys.maxsize] * d
    heappush(q, (0, start))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_node, n_dis in graph[node]:
            total_dis = distance[node] + n_dis
            if total_dis < distance[n_node]:
                distance[n_node] = total_dis
                heappush(q, (total_dis, n_node))
    
    return distance[-1]

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, dis = map(int, input().split())
    if end > d:
        continue

    graph[start].append((end, dis))

print(dijkstra(0))