from heapq import heappush, heappop

def dijkstra(n, graph):
    distance = [0] + [float('inf')] * (n - 1)
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

    return distance

def solution(n, network, repair):
    graph = [[] for _ in range(n)]

    for a, b in network:
        graph[a - 1].append((0, b - 1))
        graph[b - 1].append((0, a - 1))
    
    for a, b, t in repair:
        graph[a - 1].append((t, b - 1))
        graph[b - 1].append((t, a - 1))
    
    dis = dijkstra(n, graph)
    if float('inf') in dis:
        return -1
    return max(dis)
    
print(solution(6, [[1, 2], [3, 5], [4, 2], [5, 6]], [[3, 2, 10], [5, 4, 15]]))
print(solution(4, [[1, 2]], [[2, 3, 10], [3, 1, 12]]))