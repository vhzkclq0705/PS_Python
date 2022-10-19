# Level 2

from collections import deque

def bfs(graph, visited, n):
    cnt = 1
    q = deque([n])
    visited[n] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True

    return cnt

def solution(n, wires):
    ans = n
    graph = [[] for _ in range(n + 1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        visited = [False] * (n + 1)
        visited[wire[1]] = True
        result = bfs(graph, visited, wire[0])

        if abs(result - (n - result)) < ans:
            ans = abs(result - (n - result))

    return ans

n1 = 9
wires1 = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n1, wires1))

n2 = 4
wires2 = [[1,2],[2,3],[3,4]]
print(solution(n2, wires2))

n3 = 7
wires3 = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
print(solution(n3, wires3))