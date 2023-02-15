# Gold 3 - 고속철도 설계하기

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

n = int(input())
parent = list(range(n))
edge = []
total = 0
ans = []

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(i + 1, n):
        if s[j] < 0:
            union(i, j)
            total += -s[j]
        else:
            edge.append((s[j], i, j))

for cost, a, b in sorted(edge):
    if find(a) != find(b):
        union(a, b)
        total += cost
        ans.append((a + 1, b + 1))

print(total, len(ans))
for i in ans:
    print(*i)