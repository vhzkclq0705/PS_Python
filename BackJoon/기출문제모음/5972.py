# GOlD 5 - 택배 배송

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra():
    q = []
    heappush(q, (0, 0))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            total_dis = distance[node] + n_dis
            if distance[n_node] > total_dis:
                distance[n_node] = total_dis
                heappush(q, (total_dis, n_node))
    
    return distance[n - 1]

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [0] + [sys.maxsize] * n

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a - 1].append((t, b - 1))
    graph[b - 1].append((t, a - 1))

print(dijkstra())