# Gold 4 - 도시 건설

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = list(range(n))
edge = []
total, MST, cnt = 0, 0, 0

for _ in range(m):
    a, b, t = map(int, input().split())
    total += t
    edge.append((t, a - 1, b - 1))          

for cost, a, b in sorted(edge):
    if find(a) != find(b):
        union(a, b)
        MST += cost
        cnt += 1

print(total - MST if cnt == n - 1 else -1)