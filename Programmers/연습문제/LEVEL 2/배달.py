# LEVEL 2

from heapq import heappush, heappop

def dijkstra(n, graph):
    distance = [0] + [float('inf')] * (n-1)
    q = []
    heappush(q, (0, 0))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            total_dis = distance[node] + n_dis
            if total_dis < distance[n_node]:
                distance[n_node] = total_dis
                heappush(q, (total_dis, n_node))

    return distance

def solution(N, road, K):
    graph = [[] for _ in range(N)]

    for a, b, c in road:
        graph[a-1].append((c, b-1))
        graph[b-1].append((c, a-1))

    return len(list(filter(lambda x: x <= K, dijkstra(N, graph))))