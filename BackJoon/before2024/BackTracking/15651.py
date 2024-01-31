# Silver 3 - N과 M (3)

# Permutation
from itertools import product

n, m = map(int, input().split())
s = [i for i in range(1, n + 1)]

for per in product(s, repeat=m):
    print(*per)

# BackTracking
n, m = map(int, input().split())
s = []

def bt():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(1, n + 1):
        s.append(i)
        bt()
        s.pop()

bt()