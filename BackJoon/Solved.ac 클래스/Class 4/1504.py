# Gold 4 - 특정한 최단 경로

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start, end, flag):
    q = []
    distance = [0] + [sys.maxsize] * n
    distance[start] = 0
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
 
    if start == 1 and distance[-1] == sys.maxsize:
        print(-1)
        exit()
    
    return (distance[v1], distance[v2]) if not flag else (distance[end], distance[n])

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

v1, v2 = map(int, input().split())

a1, b1 = dijkstra(1, 0, False)
a2, c1 = dijkstra(v1, v2, True)
b2, c2 = dijkstra(v2, v1, True)

print(min(a1 + a2 + c2, b1 + b2 + c1))