# Gold 2 - 트리의 지름

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance = [0] + [sys.maxsize] * n
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

    far = max(distance)
    return far, distance.index(far)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    s = list(map(int, input().split()))[:-1]

    for i in range(1, len(s), 2):
        graph[s[0]].append((s[i + 1], s[i]))

a, idx = dijkstra(1)
b, _ = dijkstra(idx)

print(b)