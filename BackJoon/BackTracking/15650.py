# Silver 3 - N과 M (2)

# Combination
from itertools import combinations

n, m = map(int, input().split())
s = [i for i in range(1, n + 1)]

for com in combinations(s, m):
    print(*map(int, com))

# BackTracking
n, m = map(int, input().split())
s = []

def bt(v):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(v, n + 1):
        s.append(i)
        bt(i + 1)
        s.pop()

bt(1)