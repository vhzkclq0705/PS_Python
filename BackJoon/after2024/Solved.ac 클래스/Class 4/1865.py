# Gold 3 - 웜홀

import sys
input = sys.stdin.readline

def bellman_ford(start):
    distance[start] = 0

    for i in range(n):
        for now, next, dis in graph:
            total_dis = distance[now] + dis
            if total_dis < distance[next]:
                distance[next] = total_dis
                if i == n - 1:
                    return 'YES'
    
    return 'NO'

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = []
    distance = [0] + [sys.maxsize] * n

    for _ in range(m):
        a, b, t = map(int, input().split())
        graph.append((a, b, t))
        graph.append((b, a, t))
    
    for _ in range(w):
        a, b, t = map(int, input().split())
        graph.append((a, b, -t))
    
    print(bellman_ford(1))