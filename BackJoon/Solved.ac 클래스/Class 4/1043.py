# Gold 4 - 거짓말

import sys
input = sys.stdin.readline

def bfs(v):
    visited[v] = True

    for i in party[v]:
        if not visited[i] and v in fact:
            fact.add(i)
            bfs(i)

n, m = map(int, input().split())
fact = set(list(map(int, input().split()))[1:])
people = []
party = [set() for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    p = list(map(int, input().split()))
    people.append(p[1:])

    for i in range(p[0]):
        for j in range(p[0]):
            if i != j:
                party[p[i + 1]].add(p[j + 1])
                party[p[j + 1]].add(p[i + 1])

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

for i in people:
    for j in i:
        if j in fact:
            cnt += 1
            break

print(m - cnt)