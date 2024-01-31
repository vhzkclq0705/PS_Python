# Silver 1 - 케빈 베이컨의 6단계 법칙

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(v):
    distance = [sys.maxsize] * n
    distance[v] = 0
    q = []
    heappush(q, (0, v))

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for n_dis, n_node in friends[node]:
            total_dis = distance[node] + n_dis
            if distance[n_node] > total_dis:
                distance[n_node] = total_dis
                heappush(q, (total_dis, n_node))
    
    return sum(distance)

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
bacon = sys.maxsize
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    friends[a - 1].append((1, b - 1))
    friends[b - 1].append((1, a - 1))

for i in range(n):
    tmp = dijkstra(i)
    if tmp < bacon:
        bacon = tmp
        ans = i

print(ans + 1)