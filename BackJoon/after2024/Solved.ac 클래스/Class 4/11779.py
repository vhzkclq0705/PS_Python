# Gold 3 - 최소 비용 구하기 2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
    h = []
    distance[start] = 0
    heappush(h, (0, start))

    while h:
        dis, node = heappop(h)

        if dis > distance[node]:
            continue
        for n_dis, n_node in graph[node]:
            t_dis = n_dis + distance[node]
            if t_dis < distance[n_node]:
                distance[n_node] = t_dis
                path[n_node] = node
                heappush(h, (t_dis, n_node))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)
path = [0] * (n + 1)
ans = []

for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])

cur = end
while cur:
    ans.append(cur)
    cur = path[cur]

print(len(ans))
print(*reversed(ans))