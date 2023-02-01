# Gold 3 - 파티

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start, graph):
    q = []
    distance = [0] + [sys.maxsize] * n
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for next_node, next_dis in graph[node]:
            total_dis = distance[node] + next_dis
            if total_dis < distance[next_node]:
                distance[next_node] = total_dis
                heappush(q, (total_dis, next_node))
    
    return distance[1:]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # x -> 각 노드
back_graph = [[] for _ in range(n + 1)] # 각 노드 -> x

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    back_graph[b].append((a, t))

dis = dijkstra(x, graph)
back_dis = dijkstra(x, back_graph)

print(max([dis[i] + back_dis[i] for i in range(n)]))