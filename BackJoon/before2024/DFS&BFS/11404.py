# Gold 4 - 플로이드

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c
    # graph[a - 1][b - 1] = min(c, graph[a - 1][b - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    graph[i][i] = 0
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
    
    print(*graph[i])