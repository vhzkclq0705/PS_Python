# Gold 3 - 안정적인 네트워크

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
        
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = list(range(n))
edge = []
x = 0
ans = []

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    union(a, b)

for i in range(n):
    s = list(map(int, input().split()))
    if i == 0:
        continue
    
    for j in range(i + 1, n):
        edge.append((s[j], i, j))

for cost, a, b in sorted(edge):
    if find(a) != find(b):
        union(a, b)
        x += cost
        ans.append((b, a))

print(x, len(ans))
[print(a + 1, b + 1) for a, b in ans]