# Gold 5 - 숨바꼭질 3

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([n])
    graph[n] = 0

    while q:
        x = q.popleft()

        if x == m:
            return graph[x]
        
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and graph[i] == -1:
                if i == x * 2:
                    graph[i] = graph[x]
                    q.appendleft(i)
                else:
                    graph[i] = graph[x] + 1
                    q.append(i)

n, m = map(int, input().split())
graph = [-1] * 100001

print(bfs())